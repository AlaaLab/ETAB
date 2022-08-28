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
- [ ] Training/validation/testing data split ([How should I split the data?](https://github.com/ahmedmalaa/ETAB/blob/main/docs/reproducibility_checklist.md#trainingvalidationtesting-data-split))
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

The default split ratios for all datasets in ETAB is to sample a subset of 60% for training, 10% for validation and 40% for testing. When computing the ETAB score you can change the split ratios through the parameter dictionary as shown above. You can also use split the data in your customized program using the *training_data_split* function in the *utils.data_tools* module.

#### Model-specific hyperparameters

By default, ETAB uses the backbone architectures with their default hyperparameters as specified in the [torchvision](https://pytorch.org/vision/stable/models.html) library. Links to the pre-trained weights for all backbones supported by ETAB are provided in the online [leaderboard](https://github.com/ahmedmalaa/ETAB/blob/main/docs/leaderboard.md#etab-leaderboard).

#### ETAB score weights

By default, the ETABScore function assigns equal weight to all tasks. To customize the task-specific weights, provide a dictionary of weights with task-scodes as keys to the *task_weights* argument of *ETABScore*.

#### ETAB score heads

The default task-specific heads are a [SegFormer](https://arxiv.org/abs/2105.15203) head for segmentation tasks and an RNN head for video data. To change the heads for any given task, add a "head" key to the training parameter dictionary in the code snippet above.


