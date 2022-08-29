
from etab.baselines.models import *
from etab.datasets import *
from etab.utils.visualization import *
from etab.utils.data_tools import *
from etab.utils.metrics import *

import warnings
warnings.filterwarnings("ignore")


cuda_device      = 0
device           = torch.device("cuda:%d" % cuda_device if torch.cuda.is_available() else "cpu")

dataset_codes    = dict({"E": "echonet", 
                         "C": "camus",
                         "T": "tmed"})

target_codes     = dict({"a": ["LV_seg", "LA_seg", "MY_seg"],
                         "b": [],
                         "c": [],
                         "d": []}) 


def task_code_parser(benchmark_task_code):
    
    # enable video options based on the task
    
    benchmark_params = benchmark_task_code.split("-")
    
    dataset_name     = dataset_codes[benchmark_params[2]]   
    target_name      = target_codes[benchmark_params[0][0]][int(benchmark_params[0][1])]
    view_name        = benchmark_params[1]
    
    dataset          = ETAB_dataset(name=dataset_name,
                                    target=target_name, 
                                    view=view_name,
                                    video=False,
                                    normalize=True,
                                    frame_l=224,
                                    frame_w=224,
                                    clip_l=1)
    
    
    return dataset, (dataset_name, target_name, view_name)





class ETABBenchmark:
    
    def __init__(self,
                 benchmark_task_code="a0-A4-E", 
                 n_train=50, 
                 batch_size=16,
                 train_frac=0.6,
                 val_frac=0.1,
                 learning_rate=0.001,
                 n_epoch=10,
                 backbone='ResNet-50', 
                 head="SegFormer",
                 ckpt_dir="latest_model"):
        
    
        # first, create the dataset for the task by 
    
        self.dataset, benchmark_params = task_code_parser(benchmark_task_code=benchmark_task_code)
        self.model                     = ETABmodel(task="segmentation",
                                                   backbone=backbone, 
                                                   head=head)
        
        self.dataset_name  = benchmark_params[0]
        self.target_name   = benchmark_params[1]   
        self.view_name     = benchmark_params[2] 
        
        self.backbone      = backbone
        self.head          = head
        self.task_code     = benchmark_task_code
        self.n_train       = n_train 
        self.batch_size    = batch_size
        self.train_frac    = train_frac
        self.val_frac      = val_frac
        self.learning_rate = learning_rate
        self.n_epoch       = n_epoch
        
        self.ckpt_dir      = ckpt_dir #self.task_code + "_" + self.backbone + "_" + self.head
        
    
    def run(self, freeze_backbone=False, verbose=True):
        
        print("|| ETAB benchmark >>> Loading", str(self.n_train), "echocardiograms with", self.view_name, "views from the", self.dataset_name, "dataset")
        
        self.dataset.load_data(n_clips=self.n_train)

        self.train_loader, self.valid_loader, self.test_loader = training_data_split(self.dataset.data, 
                                                                                     train_frac=self.train_frac, 
                                                                                     val_frac=self.val_frac, 
                                                                                     batch_size=self.batch_size, 
                                                                                     return_loaders=True)
        
        
        print("|| ETAB benchmark >>> Training a", self.backbone, "backbone with a", self.head, "head")
        
        if freeze_backbone:
            
            self.model.freeze_backbone()
            
        
        self.model.fit(train_loader=self.train_loader, 
                       valid_loader=self.valid_loader, 
                       task_code=self.task_code, 
                       n_epoch=self.n_epoch,
                       learning_rate=self.learning_rate,
                       ckpt_dir=self.ckpt_dir,
                       device=device, 
                       verbose=verbose)
    
    
    def evaluate(self):
    
        return evaluate_model(self.model, self.test_loader)
    
    
    def switch_benchmark(self, benchmark_task_code="a0-A4-C", head=None, **kwargs):
        
        optional_args = ["n_train", "batch_size", "train_frac", "val_frac", 
                         "learning_rate", "n_epoch", "backbone"]
        
        self.dataset, benchmark_params = task_code_parser(benchmark_task_code=benchmark_task_code)
        
        self.dataset_name  = benchmark_params[0]
        self.target_name   = benchmark_params[1]   
        self.view_name     = benchmark_params[2] 
        
        self.__dict__.update(kwargs)
         
        if head is not None:
            
            self.model.switch_head(head)





