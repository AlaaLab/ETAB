
import sys
import os
import requests
import config

# replace with pip install library
from etab.utils.callbacks import *
from etab.baselines.models import *
from etab.datasets import *
import etab

import argparse
import warnings
warnings.filterwarnings("ignore")


if torch.cuda.is_available():
    
    print("GPU(s) available: ", torch.cuda.get_device_name())
    
else:
    
    print("No GPUs available")



cuda_device      = 0
device           = torch.device("cuda:%d" % cuda_device if torch.cuda.is_available() else "cpu")

    
def train_baseline(model,
                   train_loader, 
                   valid_loader, 
                   task_code, 
                   callbacks,
                   n_epoch, 
                   learning_rate,
                   backbone_type):
    
    save_base_dir = 'checkpoints'
    # Reload the pretrained network and freeze it except for its head.
    
    seg_tasks     = ["0", "1", "2"]
    class_tasks   = ["3", "4", "5", "6"]
    
    if task_code[-1] in seg_tasks:
        
        epoch_metric = ['f1', torchmetrics.JaccardIndex(num_classes=2)]
        optimizer    = optim.SGD(model.parameters(), lr=learning_rate, weight_decay=0.001)
    
    else:
        
        epoch_metric = ['f1']
        optimizer    = optim.SGD(model.fc.parameters(), lr=learning_rate, weight_decay=0.001)

    # Saves everything into ./saves/cub200_resnet18_experiment
    save_path     = os.path.join(save_base_dir, task_code + "_" + backbone_type + "_target")

    
    loss_function = nn.CrossEntropyLoss()

    model_        = Model(model, 
                          optimizer, 
                          loss_function,
                          batch_metrics=['accuracy'], 
                          epoch_metrics=epoch_metric,
                          device=device)
    
    model_.fit_generator(train_loader, 
                         valid_loader, 
                         epochs=n_epoch, 
                         callbacks=callbacks)
    
    return model_    
    
    

def get_args_parser():

    
    parser                = argparse.ArgumentParser('ETAB-benchmarking', add_help=False)
    
    # Benchmark parameters
        
    parser.add_argument('--source', default="EA40", type=str, help='Code for source task')
    parser.add_argument('--target', default="CA45", type=str, help='Code for target task')
    parser.add_argument('--backbone', default="resnet50", type=str, help='Backbone representation')
    
    # Training parameters
    parser.add_argument('--train', default=.6, type=float, help='Training fraction')
    parser.add_argument('--val', default=.5, type=float, help='Validation fraction')    
    
    # Optimizer parameters
    parser.add_argument('--epochs', default=10, type=int)
    parser.add_argument('--batch', default=32, type=int)
    parser.add_argument('--lr', type=float, default=1e-2, help='learning rate (absolute lr)')
    
    return parser


# add logger and docker

def main(args):
    
    print("Available echocardiography data sets: ", etab.datasets.available_datasets)
    
    # read all input parameters
    
    source_task           = args.source
    target_task           = args.target
    backbone_type         = args.backbone
    batch_size            = args.batch
    learning_rate         = args.lr
    n_epoch               = args.epochs
    
    train_frac            = args.train
    val_frac              = args.val
    
    benchmark_task        = source_task + target_task
        

    # load source and target data, and create train/test splits
    
    print("Loading source and target data sets...")
    
    source_dataset, target_dataset        = prepare_benchmark_data(source_task=source_task, 
                                                                   target_task=target_task)

    
    source_train, source_val, source_test = ETAB_train_test_split(source_dataset, 
                                                                  train_frac=train_frac, 
                                                                  val_frac=val_frac)

    target_train, target_val, target_test = ETAB_train_test_split(target_dataset, 
                                                                  train_frac=train_frac, 
                                                                  val_frac=val_frac)
    
    
    source_train_loader  = DataLoader(source_train, batch_size=batch_size, num_workers=8, shuffle=True)
    source_valid_loader  = DataLoader(source_val, batch_size=batch_size, num_workers=8)
    source_test_loader   = DataLoader(source_test, batch_size=batch_size, num_workers=8)

    target_train_loader  = DataLoader(target_train, batch_size=batch_size, num_workers=8, shuffle=True)
    target_valid_loader  = DataLoader(target_val, batch_size=batch_size, num_workers=8)
    target_test_loader   = DataLoader(target_test, batch_size=batch_size, num_workers=8)
    
    print("Data loading complete!")
    
    
    # Run the source task
    
    print("Fitting representation on source task")
    
    source_backbone      = prepare_ETAB_model(backbone_type, 
                                              pretrained=True, 
                                              mode="segmentation",
                                              num_classes=2)
    
    callbacks            = init_callbacks(benchmark_task)
    
    
    source_model         = train_baseline(source_backbone,
                                          source_train_loader, 
                                          source_valid_loader, 
                                          task_code=source_task, 
                                          callbacks=callbacks,
                                          n_epoch=n_epoch, 
                                          learning_rate=learning_rate,
                                          backbone_type=backbone_type)                                   
                                    
    
    # Run the target task
    
    print("Attaching a task-specific head and tuning the representation on the target task...")
    
    target_model         = attach_head(source_backbone, 
                                       backbone_type=backbone_type, 
                                       source_mode="segmentation",
                                       target_mode="classification", 
                                       num_classes=2)
    
    freeze_weights(target_model)
    
    callbacks            = init_callbacks(benchmark_task)
    target_model         = train_baseline(target_model, 
                                          target_train_loader,
                                          target_valid_loader,
                                          task_code=target_task, 
                                          callbacks=callbacks,
                                          n_epoch=n_epoch,
                                          learning_rate=learning_rate,
                                          backbone_type=backbone_type)
    
    print("Benchmark task complete!")
    

if __name__ == '__main__':
    
    args = get_args_parser()
    args = args.parse_args()

    main(args)