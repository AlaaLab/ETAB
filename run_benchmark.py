
import sys
import os
import requests
import config

# replace with pip install library
import etab
from etab.utils.callbacks import *
from etab.baselines.models import *
from etab.datasets import *
from etab.benchmarks import *


import argparse
import warnings
warnings.filterwarnings("ignore")


if torch.cuda.is_available():
    
    print("GPU(s) available: ", torch.cuda.get_device_name())
    
else:
    
    print("No GPUs available")



cuda_device      = 0
device           = torch.device("cuda:%d" % cuda_device if torch.cuda.is_available() else "cpu")



def get_args_parser():
    
    # command
    
    # python run_benchmark.py --task "a0-A4-E" --backbone "ResNet-50" --head "U-Net" --freeze_backbone False \
    #                         --train_frac 0.6 --val_frac 0.1 --lr 0.001 --epochs 100 --batch 32

    
    parser                = argparse.ArgumentParser('ETAB-benchmarking', add_help=False)
    
    # Benchmark parameters
        
    parser.add_argument('--task', default="a0-A4-E", type=str, help='Code for the benchmark task')
    parser.add_argument('--backbone', default="ResNet-50", type=str, help='Backbone representation')
    parser.add_argument('--head', default="SegFormer", type=str, help='Task-specific head')
    parser.add_argument('--freeze_backbone', default=False, type=bool, help='Freeze the backbone representation?')
    
    
    # Training parameters
    parser.add_argument('--nsample', default=100, type=int, help='Number of echocardiograms to be loaded')
    parser.add_argument('--train', default=.6, type=float, help='Training fraction')
    parser.add_argument('--val', default=.1, type=float, help='Validation fraction')    
    
    # Optimizer parameters
    parser.add_argument('--epochs', default=10, type=int)
    parser.add_argument('--batch', default=32, type=int)
    parser.add_argument('--lr', type=float, default=1e-3, help='learning rate (absolute lr)')
    
    # Adaptation parameters
    parser.add_argument('--source_task', default="None", type=str, help='Code for source task')
    parser.add_argument('--target_task', default="None", type=str, help='Code for target task')
    parser.add_argument('--source_head', default="None", type=str, help='Head for source task')
    parser.add_argument('--target_head', default="None", type=str, help='Head for target task')
    
    
    return parser


# add logger and docker

def main(args):
    
    # command
    
    # python run_benchmark.py --task "a0-A4-E" --backbone "ResNet-50" --head "U-Net" --freeze_backbone False \
    #                         --train_frac 0.6 --val_frac 0.1 --lr 0.001 --epochs 100 --batch 32
    
    #print("Available echocardiography data sets: ", etab.datasets.available_datasets)
    
    # read all input parameters
    
    task_code             = args.task
    backbone              = args.backbone
    head                  = args.head
    batch_size            = args.batch
    learning_rate         = args.lr
    n_epoch               = args.epochs
    freeze_backbone       = args.freeze_backbone
    
    source_task           = args.source_task
    target_task           = args.target_task
    source_head           = args.source_head
    target_head           = args.target_head
    
    train_frac            = args.train
    val_frac              = args.val   
    n_samples             = args.nsample
    
    # override task code it a source is specified

    if (source_task == "None"):

        source_task       = task_code
        source_head       = head
        
    elif source_head == "None":
        
        source_head       = head
        
    
    # create an instance of a benchmark class
    
    benchmark_task = ETABBenchmark(benchmark_task_code=source_task, 
                                   n_train=n_samples, 
                                   batch_size=batch_size,
                                   train_frac=train_frac,
                                   val_frac=val_frac,
                                   learning_rate=learning_rate,
                                   n_epoch=n_epoch,
                                   backbone=backbone, 
                                   head=source_head)
    
    # run the benchmark experiment
    
    benchmark_task.run(freeze_backbone)
    
    # evaluate model
    
    score = benchmark_task.evaluate()
    
    print("|| ETAB benchmark >>> Model score is:", score)
    
    if (target_task != "None"):
        
        target_head  = source_head if target_head == "None" else target_head
        
        benchmark_task.switch_benchmark(benchmark_task_code=target_task, head=target_head)
        benchmark_task.run(freeze_backbone)
        
        target_score = benchmark_task.evaluate()
        
        print("|| ETAB benchmark >>> Model score on target task is:", target_score)
        
    

if __name__ == '__main__':
    
    args = get_args_parser()
    args = args.parse_args()

    main(args)