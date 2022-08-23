from sklearn.model_selection import train_test_split
from skimage.color import gray2rgb, rgb2gray
from PIL import Image
import torchvision.transforms as transforms
from torch.utils.data import Subset, DataLoader
import pickle

import config
from etab.utils.echonet_loader import *

def training_data_split(dataset, train_frac=0.5, val_frac=0.1, batch_size=32, return_loaders=False):
    
    if type(dataset[0][1]) is list:
        
        dataset = [(dataset[k][0], dataset[k][1][0]) for k in range(len(dataset))]
    
    train_indices, valid_test_indices = train_test_split(np.arange(len(dataset)),
                                                         train_size=train_frac,
                                                         random_state=42)

    # We take 20% for the validation dataset and 20% for the test dataset
    # (i.e. 50% of the remaining 40%).
    
    valid_indices, test_indices       = train_test_split(valid_test_indices,
                                                         train_size=val_frac / (1-train_frac),
                                                         random_state=42)

    train_dataset = Subset(dataset, train_indices)
    valid_dataset = Subset(dataset, valid_indices)
    test_dataset  = Subset(dataset, test_indices)
    
    if return_loaders:
        
        train_loader  = DataLoader(train_dataset, batch_size=batch_size, num_workers=8, shuffle=True)
        valid_loader  = DataLoader(valid_dataset, batch_size=batch_size, num_workers=8)
        test_loader   = DataLoader(test_dataset, batch_size=batch_size, num_workers=8)
        
        train_dataset, valid_dataset, test_dataset = train_loader, valid_loader, test_loader 
    
    return train_dataset, valid_dataset, test_dataset