
# ETAB global variables and data directories

import torchvision.models as models

echonet_dir        = "/data/echonet" 
camus_dir          = "/data/camus" 
tmed_dir           = "/data/tmed" 

ETAB_backbone_dict = dict({"resnet18": models.resnet18,
                           "resnet50": models.resnet50,
                           "alexnet": models.alexnet,
                           "vgg16": models.vgg16,
                           "densenet": models.densenet161,
                           "inception": models.inception_v3,
                           "googlenet": models.googlenet,
                           "mobilenet_v2": models.mobilenet_v2,
                           "mobilenet_v3_large": models.mobilenet_v3_large,
                           "mobilenet_v3_small": models.mobilenet_v3_small,
                           "resnext50_32x4d": models.resnext50_32x4d,
                           "wide_resnet50_2": models.wide_resnet50_2,
                           "vit_b_16": models.vit_b_16,
                           "vit_b_32": models.vit_b_32,
                           "vit_l_16": models.vit_l_16,
                           "vit_l_32": models.vit_l_32,
                           "convnext_tiny": models.convnext_tiny,
                           "convnext_small": models.convnext_small,
                           "convnext_base": models.convnext_base,
                           "convnext_large": models.convnext_large})

dataset_names      = dict({"echonet": "E", 
                           "camus": "C",
                           "tmed": "T"})
        
task_targets       = dict({"EF": "3",
                           "LV_seg": "0",
                           "MY_seg": "1",
                           "LA_seg": "2",
                           "CM": "5",
                           "AS": "6"})
