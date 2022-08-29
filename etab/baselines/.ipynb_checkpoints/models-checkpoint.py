
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.models as models
from torchvision import transforms
import config
import segmentation_models_pytorch as smp
import torchmetrics
from torch import Tensor
from torch.nn import functional as F
from semseg.models.base import BaseModel
from semseg.models.heads import * 

from etab.utils.callbacks import *

from poutyne import set_seeds, Model, ModelCheckpoint, CSVLogger, Experiment

import warnings
warnings.filterwarnings("ignore")


if torch.cuda.is_available():
    
    print("GPU(s) available: ", torch.cuda.get_device_name())
    
else:
    
    print("No GPUs available")

cuda_device      = 0
device           = torch.device("cuda:%d" % cuda_device if torch.cuda.is_available() else "cpu")



class ETABmodel(BaseModel):
    
    def __init__(self, 
                 task: str = "segmentation", 
                 backbone: str = 'ResNet-50', 
                 head: str = "UPer", 
                 num_classes: int = 2):
        
        super().__init__(backbone, num_classes)
        
        self.num_classes = num_classes
        
        self.model       = None
        self.decode_head = eval(head + "Head")(self.backbone.channels, 256, num_classes)
        
        self.apply(self._init_weights)

    def forward(self, x: Tensor) -> Tensor:
        
        y = self.backbone(x)
        y = self.decode_head(y)   # 4x reduction in image size
        y = F.interpolate(y, size=x.shape[2:], mode='bilinear', align_corners=False)    # to original image shape
        
        return y
    
    
    def fit(self, 
            train_loader, 
            valid_loader, 
            task_code="a0-A4-E", 
            n_epoch=50,
            learning_rate=1e-2,
            ckpt_dir=None,
            device="cpu",
            verbose=True):
        
        
        callbacks   = init_callbacks(ckpt_dir)
        self.device = device
        
        save_base_dir = 'checkpoints'
        # Reload the pretrained network and freeze it except for its head.
    
        optimizer    = optim.SGD(self.parameters(), lr=learning_rate, weight_decay=0.001)
    
    
        if task_code[0] == "a":

            epoch_metric = ['f1', torchmetrics.JaccardIndex(num_classes=2)]
            #optimizer    = optim.SGD(model.parameters(), lr=learning_rate, weight_decay=0.001)
    
        else:
        
            epoch_metric = ['f1']
            #optimizer    = optim.SGD(model.fc.parameters(), lr=learning_rate, weight_decay=0.001)
    
    
        # Saves everything into ./saves/cub200_resnet18_experiment
        #save_path     = os.path.join(save_base_dir, task_code + "_" + backbone_type + "_target")
        save_path     = os.path.join(save_base_dir, ckpt_dir)
    
        loss_function = nn.CrossEntropyLoss()

        self.model    = Model(self, 
                              optimizer, 
                              loss_function,
                              batch_metrics=['accuracy'], 
                              epoch_metrics=epoch_metric,
                              device=device)
    
        self.model.fit_generator(train_loader, 
                                 valid_loader, 
                                 epochs=n_epoch, 
                                 callbacks=callbacks, 
                                 verbose=verbose)
    
    def predict(self, X):
        
        return self(X.to(self.device)).argmax(1).detach().cpu() #.numpy() 
    
    
    def freeze_backbone(self):
        
        for param in self.backbone.parameters():
            
            param.requires_grad = False
            
    def switch_head(self, new_head):
        
        self.decode_head = eval(new_head + "Head")(self.backbone.channels, 256, self.num_classes)
        
        
        
#######        

def freeze_weights(model):
    
    for name, param in model.named_parameters():
        
        if not name.startswith('fc.'):
            
            param.requires_grad = False


def attach_head(backbone_representation, **kwargs): 
     
    
    if kwargs["source_mode"]=="classification":
        
        backbone_representation.fc  = nn.Linear(backbone_representation.fc.in_features, kwargs["num_classes"])
        downstream_model            = backbone_representation
        
    elif kwargs["source_mode"]=="segmentation":
        
        downstream_model = prepare_ETAB_model(kwargs["backbone_type"], 
                                              pretrained=True, 
                                              mode=kwargs["target_mode"],
                                              num_classes=kwargs["num_classes"])

        for key, param in backbone_representation.encoder.state_dict().items():
    
            if key not in downstream_model.state_dict():
        
                continue
        
            else:

                param = param.data

                downstream_model.state_dict()[key].copy_(param)   
        
    del backbone_representation
    
    return downstream_model



def prepare_ETAB_model(backbone_type, 
                       pretrained=True, 
                       adaptation="finetune", 
                       **kwargs):
    
    if kwargs["mode"]=="classification":
    
        backbone_representation     = config.ETAB_backbone_dict[backbone_type](pretrained=pretrained)
    
        downstream_model            = attach_head(backbone_representation, 
                                                  source_mode=kwargs["mode"], 
                                                  num_classes=kwargs["num_classes"])
    
        del backbone_representation
    
    elif kwargs["mode"]=="segmentation":
    
        downstream_model            = smp.Unet(backbone_type, 
                                               encoder_weights='imagenet', 
                                               classes=kwargs["num_classes"])
    
    if adaptation=="linear_probe":
        
        freeze_weights(downstream_model)
    
    return downstream_model