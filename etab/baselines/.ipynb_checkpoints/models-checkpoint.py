
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.models as models
from torchvision import transforms
import config
import segmentation_models_pytorch as smp
import torchmetrics

from poutyne import set_seeds, Model, ModelCheckpoint, CSVLogger, Experiment


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