from etab.benchmarks import *

import warnings
warnings.filterwarnings("ignore")


echonet_parameters   = dict({"n_train":7000, 
                             "batch_size":32,
                             "train_frac":0.6,
                             "val_frac":0.1,
                             "learning_rate":0.001,
                             "n_epoch":50})

camus_parameters     = dict({"n_train":450, 
                             "batch_size":32,
                             "train_frac":0.6,
                             "val_frac":0.1,
                             "learning_rate":0.001,
                             "n_epoch":50})
                               

ETAB_benchmark_tasks = dict({"a0-A4-E": echonet_parameters,
                             "a0-A4-C": echonet_parameters,
                             "a0-A2-C": echonet_parameters,
                             "a1-A4-C": echonet_parameters,
                             "a1-A2-C": echonet_parameters})




def run_one_benchmark(backbone_architecture, backbone_model, task_code, verbose, finetune=False, **kwargs):
    
    benchmark_task  = ETABBenchmark(benchmark_task_code=task_code, 
                                    n_train=kwargs["n_train"], 
                                    batch_size=kwargs["batch_size"],
                                    train_frac=kwargs["train_frac"],
                                    val_frac=kwargs["val_frac"],
                                    learning_rate=kwargs["learning_rate"],
                                    n_epoch=kwargs["n_epoch"],
                                    backbone=backbone_architecture, 
                                    head="SegFormer")
    
    if backbone_model is not None:
    
        benchmark_task.model.backbone.load_state_dict(backbone_model.state_dict(), strict=False)    
    
    benchmark_task.run(freeze_backbone= not finetune, verbose=verbose)
    
    benchmark_score = benchmark_task.evaluate()
    
    return benchmark_score


def ETABscore(backbone_architecture, backbone_model, task_weights=None, verbose=False, finetune=False):
    
    benchmark_scores = dict.fromkeys(ETAB_benchmark_tasks)
    
    for task_key in ETAB_benchmark_tasks.keys():
        
        print("|| ETAB score >> Running benchmark task:", task_key)
        
        benchmark_score_           = run_one_benchmark(backbone_architecture, backbone_model, task_key, finetune=finetune, **ETAB_benchmark_tasks[task_key], verbose=verbose)
        benchmark_scores[task_key] = benchmark_score_
        
        print("|| ETAB score >> Task scorek:", benchmark_score_)
    
    ETAB_score       = np.array(list(benchmark_scores.values())).mean()
    
    return ETAB_score, benchmark_scores 











