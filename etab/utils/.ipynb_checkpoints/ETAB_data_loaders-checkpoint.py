
from sklearn.model_selection import train_test_split
from skimage.color import gray2rgb, rgb2gray
from PIL import Image
import torchvision.transforms as transforms
from torch.utils.data import Subset, DataLoader
import pickle

import config
from etab.utils.echonet_loader import *


def prepare_image(index, dataset, segment_index=1, IMG_SIZE=224, img_type="4CH_ED", normalize=True):

    imagenet_mean  = np.array([0.485, 0.456, 0.406])
    imagenet_std   = np.array([0.229, 0.224, 0.225])

    input_resize   = transforms.Resize((IMG_SIZE, IMG_SIZE))
    convert_tensor = transforms.ToTensor()

    test_img_      = input_resize(Image.fromarray(np.uint8(gray2rgb(dataset[index][img_type]).squeeze(0))).convert('RGB'))
    test_img       = torch.einsum("chw->hwc", convert_tensor(test_img_))

    test_seg_      = input_resize(Image.fromarray(np.uint8((dataset[index][img_type + "_gt"]==segment_index)*1).squeeze(0)))#.convert('RGB'))
    test_seg_      = torch.einsum("chw->hwc", convert_tensor(test_seg_)) 
    test_seg       = test_seg_ / torch.max(test_seg_)
    
    if normalize:
        
        test_img   = test_img - imagenet_mean
        test_img   = test_img / imagenet_std
    
    test_img       = torch.einsum("hwc->chw", test_img)
    test_seg       = (torch.einsum("hwc->chw", test_seg) > 0) * 1
    
    return test_img.float(), [test_seg.view((IMG_SIZE, IMG_SIZE)).long()]


def load_ETAB_dataset(dataset_type="C", echo_view="A4", label_type="0", n_clips=None, clip_l=1, normalize=True):
    
    # "LargeFrame", "LargeTrace"
    # ``EF'', ``EDV'', ``ESV'', ``LargeIndex'',
    # ``SmallIndex'', ``LargeFrame'', ``SmallFrame'', ``LargeTrace'',
    
    if dataset_type=="C":
        
        segment_names   = dict({"A4": "4CH_", "A2": "2CH_"})
        anatomic_ID     = dict({"0": 1, "1": 2, "2": 3,
                                "3": 1, "4": 1, "5": 1, "6": 1}) # 0: LV, 1: LA, 2: MY
        
        with open(config.camus_dir, "rb") as f:
            
            raw_dataset = pickle.load(f)
            
        dataset  = [prepare_image(k, 
                                  raw_dataset, 
                                  segment_index=anatomic_ID[label_type], 
                                  IMG_SIZE=224, 
                                  img_type=segment_names[echo_view] + "ED", 
                                  normalize=normalize) for k in range(len(raw_dataset))]    
        
        if label_type=="5":
        
            LVef     = [(float(raw_dataset[k]["info_2CH"]["LVef"]) < 50) * 1 for k in range(len(raw_dataset))]
            dataset  = [(dataset[k][0], LVef[k]) for k in range(len(dataset))]
            
            
    elif dataset_type=="E":
        
        if label_type == "0":
        
            dataset  = load_segmented_data(data_dir=config.echonet_dir, 
                                           n_clips=n_clips, 
                                           IMG_SIZE=224,
                                           normalize=normalize,
                                           targets=["LargeFrame", "LargeTrace"])
        
        elif label_type == "3":
        
            dataset  = load_EF_data(data_dir=config.echonet_dir,  
                                    n_clips=n_clips, 
                                    IMG_SIZE=224, 
                                    n_frames=clip_l,
                                    normalize=normalize,
                                    targets=["EF", "SmallIndex", "LargeIndex"])
        
    return dataset    

def prepare_benchmark_data(source_task="EA40", target_task="CA45"):
    
    target_dataset       = load_ETAB_dataset(dataset_type=target_task[0], 
                                             echo_view=target_task[1:3], 
                                             label_type=target_task[-1])
    
    if source_task is not None:
        
        source_dataset   = load_ETAB_dataset(dataset_type=source_task[0], 
                                             echo_view=source_task[1:3], 
                                             label_type=source_task[-1])
    
    
    return source_dataset, target_dataset

# We take 60% of the dataset for the training dataset

def ETAB_train_test_split(dataset, train_frac=0.6, val_frac=0.5):
    
    train_indices, valid_test_indices = train_test_split(np.arange(len(dataset)),
                                                         train_size=train_frac,
                                                         random_state=42)

    # We take 20% for the validation dataset and 20% for the test dataset
    # (i.e. 50% of the remaining 40%).
    
    valid_indices, test_indices       = train_test_split(valid_test_indices,
                                                         train_size=val_frac,
                                                         random_state=42)

    train_dataset = Subset(dataset, train_indices)
    valid_dataset = Subset(dataset, valid_indices)
    test_dataset  = Subset(dataset, test_indices)
    
    return train_dataset, valid_dataset, test_dataset