import config
from etab.utils.ETAB_data_loaders import *
from etab.utils.callbacks import *

available_datasets = ["EchoNet", "CAMUS", "TMED"]

class ETAB_dataset:
    
    """
    Generic class with common functionalities for echo data sets 
    
    """
    
    """
    
    Option 1: "echonet"
    
    The EchoNet dataset, introduced in [1, 2], comprises one apical-4 chamber (AP4CH) 2D gray-scale video is extracted from each echo study. 
    A total of 10,036 videos are collected from 10,036 distinct individuals who underwent echocardiography between 2006 and 2018 as part of 
    routine care at a University Hospital. Individuals in the data set were selected at random from hospital records cardiac function assessments 
    and calculations obtained by a registered sonographer and verified by a level-3 echocardiographer are provided. 
    
    Data is accessible via: https://echonet.github.io/echoNet/.
    
    The "echonet" class is part of the etab.datasets module and contains the functionalities required for loading and processing the EchoNet data set.

    
    References:
    -----------
    
    [1] David Ouyang, Bryan He, Amirata Ghorbani, Matt P Lungren, Euan A Ashley, David H Liang, and James Y Zou. 
        Echonet-dynamic: a large new cardiac motion video data resource for medical machine learning. 
        In NeurIPS ML4H Workshop: Vancouver, BC, Canada, 2019.
        
    [2] David Ouyang, Bryan He, Amirata Ghorbani, Neal Yuan, Joseph Ebinger, Curtis P Langlotz, Paul A Heidenreich, Robert A Harrington, 
        David H Liang, Euan A Ashley, et al. Video-based AI for beat-to-beat assessment of cardiac function. Nature, 580(7802):252–256, 2020.

    """
    
    def __init__(self,
                 name="echonet",
                 target="EF",
                 view="A4CH",
                 video=False,
                 normalize=True,
                 frame_l=224,
                 frame_w=224,
                 clip_l=16, 
                 fps=50,
                 padding=None):

        self.name      = name
        self.target    = target 
        self.view      = view
        self.video     = video
        self.normalize = normalize
        self.frame_l   = frame_l
        self.frame_w   = frame_w
        self.clip_l    = clip_l
        self.fps       = fps
        self.padding   = padding
        
        
    def load_data(self, n_clips=None, **kwargs):
        
        """
        
        ** Generic function for loading echo data sets **
        
        :param n_clips: Number of distinct echocardiography clips to be loaded 
        
        """    
        
        self.data      = load_ETAB_dataset(dataset_type=config.dataset_names[self.name], 
                                           echo_view=self.view, 
                                           label_type=config.task_targets[self.target],
                                           n_clips=n_clips,
                                           clip_l=self.clip_l,
                                           normalize=self.normalize)
        
        
        

        
