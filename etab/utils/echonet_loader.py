"""EchoNet-Dynamic Dataset."""
# Code is adapted from: https://github.com/echonet/dynamic

import os
import collections
import pandas
import torch
import numpy as np
import skimage.draw
import torchvision
import etab.utils.echonet
from skimage.color import rgb2gray, gray2rgb
import torchvision.transforms as T
from PIL import Image
import matplotlib.image as mpimg

from os import listdir
from os.path import isfile, join
import numpy as np
from os import listdir
from os.path import isfile, join
import cv2
import xml.etree.ElementTree as ET
import config

imagenet_mean  = np.array([0.485, 0.456, 0.406])
imagenet_std   = np.array([0.229, 0.224, 0.225])


class Echo(torchvision.datasets.VisionDataset):
    """EchoNet-Dynamic Dataset.
    Args:
        root (string): Root directory of dataset (defaults to `echonet.config.DATA_DIR`)
        split (string): One of {``train'', ``val'', ``test'', ``all'', or ``external_test''}
        target_type (string or list, optional): Type of target to use,
            ``Filename'', ``EF'', ``EDV'', ``ESV'', ``LargeIndex'',
            ``SmallIndex'', ``LargeFrame'', ``SmallFrame'', ``LargeTrace'',
            or ``SmallTrace''
            Can also be a list to output a tuple with all specified target types.
            The targets represent:
                ``Filename'' (string): filename of video
                ``EF'' (float): ejection fraction
                ``EDV'' (float): end-diastolic volume
                ``ESV'' (float): end-systolic volume
                ``LargeIndex'' (int): index of large (diastolic) frame in video
                ``SmallIndex'' (int): index of small (systolic) frame in video
                ``LargeFrame'' (np.array shape=(3, height, width)): normalized large (diastolic) frame
                ``SmallFrame'' (np.array shape=(3, height, width)): normalized small (systolic) frame
                ``LargeTrace'' (np.array shape=(height, width)): left ventricle large (diastolic) segmentation
                    value of 0 indicates pixel is outside left ventricle
                             1 indicates pixel is inside left ventricle
                ``SmallTrace'' (np.array shape=(height, width)): left ventricle small (systolic) segmentation
                    value of 0 indicates pixel is outside left ventricle
                             1 indicates pixel is inside left ventricle
            Defaults to ``EF''.
        mean (int, float, or np.array shape=(3,), optional): means for all (if scalar) or each (if np.array) channel.
            Used for normalizing the video. Defaults to 0 (video is not shifted).
        std (int, float, or np.array shape=(3,), optional): standard deviation for all (if scalar) or each (if np.array) channel.
            Used for normalizing the video. Defaults to 0 (video is not scaled).
        length (int or None, optional): Number of frames to clip from video. If ``None'', longest possible clip is returned.
            Defaults to 16.
        period (int, optional): Sampling period for taking a clip from the video (i.e. every ``period''-th frame is taken)
            Defaults to 2.
        max_length (int or None, optional): Maximum number of frames to clip from video (main use is for shortening excessively
            long videos when ``length'' is set to None). If ``None'', shortening is not applied to any video.
            Defaults to 250.
        clips (int, optional): Number of clips to sample. Main use is for test-time augmentation with random clips.
            Defaults to 1.
        pad (int or None, optional): Number of pixels to pad all frames on each side (used as augmentation).
            and a window of the original size is taken. If ``None'', no padding occurs.
            Defaults to ``None''.
        noise (float or None, optional): Fraction of pixels to black out as simulated noise. If ``None'', no simulated noise is added.
            Defaults to ``None''.
        target_transform (callable, optional): A function/transform that takes in the target and transforms it.
        external_test_location (string): Path to videos to use for external testing.
    """

    def __init__(self, root=None,
                 split="train", target_type="EF",
                 mean=0., std=1.,
                 length=16, period=2,
                 max_length=250,
                 clips=1,
                 pad=None,
                 noise=None,
                 target_transform=None,
                 external_test_location=None):
        if root is None:
            root = etab.utils.echonet.config.DATA_DIR

        super().__init__(root, target_transform=target_transform)

        self.split = split.upper()
        if not isinstance(target_type, list):
            target_type = [target_type]
        self.target_type = target_type
        self.mean = mean
        self.std = std
        self.length = length
        self.max_length = max_length
        self.period = period
        self.clips = clips
        self.pad = pad
        self.noise = noise
        self.target_transform = target_transform
        self.external_test_location = external_test_location

        self.fnames, self.outcome = [], []

        if self.split == "EXTERNAL_TEST":
            self.fnames = sorted(os.listdir(self.external_test_location))
        else:
            # Load video-level labels
            with open(os.path.join(self.root, "FileList.csv")) as f:
                data = pandas.read_csv(f)
            data["Split"].map(lambda x: x.upper())

            if self.split != "ALL":
                data = data[data["Split"] == self.split]

            self.header = data.columns.tolist()
            self.fnames = data["FileName"].tolist()
            self.fnames = [fn + ".avi" for fn in self.fnames if os.path.splitext(fn)[1] == ""]  # Assume avi if no suffix
            self.outcome = data.values.tolist()

            # Check that files are present
            missing = set(self.fnames) - set(os.listdir(os.path.join(self.root, "Videos")))
            if len(missing) != 0:
                print("{} videos could not be found in {}:".format(len(missing), os.path.join(self.root, "Videos")))
                for f in sorted(missing):
                    print("\t", f)
                raise FileNotFoundError(os.path.join(self.root, "Videos", sorted(missing)[0]))

            # Load traces
            self.frames = collections.defaultdict(list)
            self.trace = collections.defaultdict(_defaultdict_of_lists)

            with open(os.path.join(self.root, "VolumeTracings.csv")) as f:
                header = f.readline().strip().split(",")
                assert header == ["FileName", "X1", "Y1", "X2", "Y2", "Frame"]

                for line in f:
                    filename, x1, y1, x2, y2, frame = line.strip().split(',')
                    x1 = float(x1)
                    y1 = float(y1)
                    x2 = float(x2)
                    y2 = float(y2)
                    frame = int(frame)
                    if frame not in self.trace[filename]:
                        self.frames[filename].append(frame)
                    self.trace[filename][frame].append((x1, y1, x2, y2))
            for filename in self.frames:
                for frame in self.frames[filename]:
                    self.trace[filename][frame] = np.array(self.trace[filename][frame])

            # A small number of videos are missing traces; remove these videos
            keep = [len(self.frames[f]) >= 2 for f in self.fnames]
            self.fnames = [f for (f, k) in zip(self.fnames, keep) if k]
            self.outcome = [f for (f, k) in zip(self.outcome, keep) if k]

    def __getitem__(self, index):
        # Find filename of video
        if self.split == "EXTERNAL_TEST":
            video = os.path.join(self.external_test_location, self.fnames[index])
        elif self.split == "CLINICAL_TEST":
            video = os.path.join(self.root, "ProcessedStrainStudyA4c", self.fnames[index])
        else:
            video = os.path.join(self.root, "Videos", self.fnames[index])

        # Load video into np.array
        video = etab.utils.echonet.utils.loadvideo(video).astype(np.float32)

        # Add simulated noise (black out random pixels)
        # 0 represents black at this point (video has not been normalized yet)
        if self.noise is not None:
            n = video.shape[1] * video.shape[2] * video.shape[3]
            ind = np.random.choice(n, round(self.noise * n), replace=False)
            f = ind % video.shape[1]
            ind //= video.shape[1]
            i = ind % video.shape[2]
            ind //= video.shape[2]
            j = ind
            video[:, f, i, j] = 0

        # Apply normalization
        if isinstance(self.mean, (float, int)):
            video -= self.mean
        else:
            video -= self.mean.reshape(3, 1, 1, 1)

        if isinstance(self.std, (float, int)):
            video /= self.std
        else:
            video /= self.std.reshape(3, 1, 1, 1)

        # Set number of frames
        c, f, h, w = video.shape
        if self.length is None:
            # Take as many frames as possible
            length = f // self.period
        else:
            # Take specified number of frames
            length = self.length

        if self.max_length is not None:
            # Shorten videos to max_length
            length = min(length, self.max_length)

        if f < length * self.period:
            # Pad video with frames filled with zeros if too short
            # 0 represents the mean color (dark grey), since this is after normalization
            video = np.concatenate((video, np.zeros((c, length * self.period - f, h, w), video.dtype)), axis=1)
            c, f, h, w = video.shape  # pylint: disable=E0633

        if self.clips == "all":
            # Take all possible clips of desired length
            start = np.arange(f - (length - 1) * self.period)
        else:
            # Take random clips from video
            start = np.random.choice(f - (length - 1) * self.period, self.clips)

        # Gather targets
        target = []
        for t in self.target_type:
            key = self.fnames[index]
            if t == "Filename":
                target.append(self.fnames[index])
            elif t == "LargeIndex":
                # Traces are sorted by cross-sectional area
                # Largest (diastolic) frame is last
                target.append(np.int(self.frames[key][-1]))
            elif t == "SmallIndex":
                # Largest (diastolic) frame is first
                target.append(np.int(self.frames[key][0]))
            elif t == "LargeFrame":
                target.append(video[:, self.frames[key][-1], :, :])
            elif t == "SmallFrame":
                target.append(video[:, self.frames[key][0], :, :])
            elif t in ["LargeTrace", "SmallTrace"]:
                if t == "LargeTrace":
                    t = self.trace[key][self.frames[key][-1]]
                else:
                    t = self.trace[key][self.frames[key][0]]
                x1, y1, x2, y2 = t[:, 0], t[:, 1], t[:, 2], t[:, 3]
                x = np.concatenate((x1[1:], np.flip(x2[1:])))
                y = np.concatenate((y1[1:], np.flip(y2[1:])))

                r, c = skimage.draw.polygon(np.rint(y).astype(np.int), np.rint(x).astype(np.int), (video.shape[2], video.shape[3]))
                mask = np.zeros((video.shape[2], video.shape[3]), np.float32)
                mask[r, c] = 1
                target.append(mask)
            else:
                if self.split == "CLINICAL_TEST" or self.split == "EXTERNAL_TEST":
                    target.append(np.float32(0))
                else:
                    target.append(np.float32(self.outcome[index][self.header.index(t)]))

        if target != []:
            target = tuple(target) if len(target) > 1 else target[0]
            if self.target_transform is not None:
                target = self.target_transform(target)

        # Select clips from video
        video = tuple(video[:, s + self.period * np.arange(length), :, :] for s in start)
        if self.clips == 1:
            video = video[0]
        else:
            video = np.stack(video)

        if self.pad is not None:
            # Add padding of zeros (mean color of videos)
            # Crop of original size is taken out
            # (Used as augmentation)
            c, l, h, w = video.shape
            temp = np.zeros((c, l, h + 2 * self.pad, w + 2 * self.pad), dtype=video.dtype)
            temp[:, :, self.pad:-self.pad, self.pad:-self.pad] = video  # pylint: disable=E1130
            i, j = np.random.randint(0, 2 * self.pad, 2)
            video = temp[:, :, i:(i + h), j:(j + w)]

        return video, target

    def __len__(self):
        return len(self.fnames)

    def extra_repr(self) -> str:
        """Additional information to add at end of __repr__."""
        lines = ["Target type: {target_type}", "Split: {split}"]
        return '\n'.join(lines).format(**self.__dict__)


def _defaultdict_of_lists():
    """Returns a defaultdict of lists.
    This is used to avoid issues with Windows (if this function is anonymous,
    the Echo dataset cannot be used in a dataloader).
    """

    return collections.defaultdict(list)



"""
def load_segmented_data(data_dir, n_train=None, concatenate=True, rgb=False, IMG_SIZE=224):
    
    transform    = T.ToPILImage()
    pil_2_tensor = T.ToTensor()
    
    dataset      = Echo(root=data_dir + "/data/", target_type="SmallTrace")

    n_train      = len(dataset) if n_train is None else n_train
    
    videos       = []
    segments     = []

    for _ in range(n_train):
  
        current_video, current_trace = dataset.__getitem__(_) 
    
        if rgb:
            
            current_video, current_trace = torch.einsum('cnhw->nhwc', torch.tensor(current_video)/255)[0, :, :, :], torch.tensor(gray2rgb(current_trace))[0, :, :, :]
        
        else:
            
            current_video = torch.einsum('cnhw->nhwc', torch.tensor(current_video)/255)[0, :, :, :]                
            current_trace = torch.tensor(current_trace)

            current_video = pil_2_tensor(transform(torch.einsum('hwc->chw', current_video)).resize((IMG_SIZE, IMG_SIZE)))
            current_trace = pil_2_tensor(transform(current_trace).resize((IMG_SIZE, IMG_SIZE))).squeeze(0)

        videos.append(current_video.unsqueeze(0))
        segments.append(current_trace.unsqueeze(0))  
    
    if concatenate:
        
        videos       = torch.cat(videos)
        segments     = torch.cat(segments) 
        all_data_set = torch.cat([videos, segments], dim=1)
        
    else:
        
        all_data_set = [(videos[k].squeeze(0), segments[k].squeeze(0).type(torch.LongTensor)) for k in range(len(videos))]
    
    return all_data_set

"""

transform    = T.ToPILImage()
pil_2_tensor = T.ToTensor()

def flip_channels(video, IMG_SIZE):
  
    if video.shape[0]==1:
        
        video = video.squeeze(0)
        video = pil_2_tensor(transform(torch.einsum('hwc->chw', video)).resize((IMG_SIZE, IMG_SIZE)))
            
    else:
        
        # loop over frames
        video = [pil_2_tensor(transform(torch.einsum('hwc->chw', video[kk, :, :, :])).resize((IMG_SIZE, IMG_SIZE))).unsqueeze(0) for kk in range(video.shape[0])]
        video = torch.cat(video, dim=0)

    return video   


def load_segmented_data(data_dir, 
                        n_clips=None, 
                        IMG_SIZE=224, 
                        n_frames=1, 
                        normalize=True,
                        targets=["LargeFrame", "LargeTrace"]):

    
    dataset       = Echo(root=data_dir + "/data/", target_type=targets)
    
    n_clips       = len(dataset) if n_clips is None else n_clips
    
    videos        = []
    label         = []

    for _ in range(n_clips):
        
        current_trace  = [] 
  
        _video, _trace = dataset.__getitem__(_) 
        current_video  = torch.einsum('cnhw->nhwc', torch.tensor(_video)/255)[:n_frames, :, :, :] 
        
        if type(_trace) is not tuple:
            
            _trace = [_trace]
        
        for u in range(len(_trace)):
            
            if targets[u] in ["SmallFrame", "LargeFrame"]:
                
                _video         = torch.tensor(_trace[u])/255 #_trace[u]
                current_video  = torch.einsum('chw->hwc', _video)
            
            else:
            
                curr_trace = pil_2_tensor(transform(torch.tensor(_trace[u])).resize((IMG_SIZE, IMG_SIZE))).squeeze(0) if type(_trace[u]) != float else _trace[u]
                
                if targets[u] in ["SmallTrace", "LargeTrace"]:
                    
                    curr_trace = curr_trace.type(torch.LongTensor)

                current_trace.append(curr_trace)
        

        current_video = flip_channels(current_video.unsqueeze(0), IMG_SIZE)
        
        if normalize:
            
            current_video   = torch.einsum('chw->hwc', current_video)
            current_video   = current_video - imagenet_mean
            current_video   = current_video / imagenet_std
            current_video   = torch.einsum('hwc->chw', current_video)
        
        
        current_video = current_video.float()
        
        videos.append(current_video)
        label.append(current_trace)
    
    #all_data_set = [(videos[k].squeeze(0), (label[k][0], label[k][1].type(torch.LongTensor))) for k in range(len(videos))]
    all_data_set = [(videos[k], label[k]) for k in range(len(videos))]    

    return all_data_set



def load_EF_data(data_dir, 
                 n_clips=None, 
                 IMG_SIZE=224, 
                 n_frames=1, 
                 normalize=True,
                 targets=["EF", "SmallIndex", "LargeIndex"]):
    
    dataset       = Echo(root=data_dir + "/data/", target_type=targets)
    
    n_clips       = len(dataset) if n_clips is None else n_clips
    
    videos        = []
    label         = []

    for _ in range(n_clips):
        
        _video, _trace = dataset.__getitem__(_) 
        current_video  = torch.einsum('cnhw->nhwc', torch.tensor(_video)/255)[:n_frames, :, :, :] 
        current_video  = flip_channels(current_video, IMG_SIZE)
        
        videos.append(current_video.unsqueeze(0))
        label.append(_trace)
    
    all_data_set = [(videos[k].squeeze(0), label[k]) for k in range(len(videos))]   

    return all_data_set




















