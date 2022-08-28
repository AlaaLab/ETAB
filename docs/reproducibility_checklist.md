---------------

<p align="center">
  <img width="280" height="160" src="assets/etab_logo.png" />
</p>

<h1 align="center">
    <b> ETAB Reproducibility Checklist </b>
</h1>

### Things to check before running your experiment!

To ensure the reproducibility and consistency of benchmarking experiments conducted using ETAB, we recommend that you check and report the following experimental parameters when using ETAB in your research.

- [ ] Benchmark task-specific training parameters ([How do I set the training parameters for each task?](https://github.com/ahmedmalaa/ETAB/blob/main/docs/reproducibility_checklist.md#benchmark-task-specific-training-parameters))
- [ ] Training/validation/testing data split ([How should I split the data?](https://github.com/ahmedmalaa/ETAB/blob/main/docs/reproducibility_checklist.md#benchmark-task-specific-training-parameters))
- [ ] Model-specific hyperparameters
- [ ] ETAB score weights
- [ ] ETAB score heads

#### Benchmark task-specific training parameters

The default optimization and training parameters in the ETAB software are:

```python

train_frac    = 0.6
val_frac      = 0.1
learning_rate = 0.001
batch_size    = 32
n_epoch       = 50

```

Training is conducted with an SGD optimizer, and the final weights are picked based on best performance on validation data. To change the training parameters, create a dictionary of parameter values as follows:

```python

training_params_dict = dict({"batch_size":32,
                             "train_frac":0.6,
                             "val_frac":0.1,
                             "learning_rate":0.001,
                             "n_epoch":50})

```

In the example below, we create a dictionary of task-specific training parameters with the task codes as the keys. You can also customize the training parameters for each task by feeding in a different parameters' dictionary for each task.

```
ETAB_benchmark_tasks = dict({"a0-A4-E": training_params_dict,
                             "a0-A4-C": training_params_dict,
                             "a0-A2-C": training_params_dict,
                             "a1-A4-C": training_params_dict,
                             "a1-A2-C": training_params_dict})

```

The parameters' dictionary can then be passed to the *ETABScore* function as follows:

```python

ETAB_score, benchmark_scores = ETABscore(backbone_architecture, 
                                         backbone_model, 
                                         task_weights=None, 
                                         verbose=False, 
                                         finetune=False,
                                         **ETAB_benchmark_tasks)

```

#### Training/validation/testing data split
                             
