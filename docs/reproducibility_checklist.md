---------------

<p align="center">
  <img width="280" height="160" src="assets/etab_logo.png" />
</p>

<h1 align="center">
    <b> ETAB Reproducibility Checklist </b>
</h1>

### Things to check before running your experiment!

To ensure the reproducibility and consistency of benchmarking experiments conducted using ETAB, we recommend that you check and report the following experimental parameters when using ETAB in your research.

- [ ] Benchmark task-specific training parameters
- [ ] Training/validation/testing data split
- [ ] Model-specific hyperparameters
- [ ] ETAB score weights
- [ ] ETAB score heads
- [ ] Random seeds

#### Benchmark task-specific training parameters

The default optimization and training parameters in the ETAB software are:

```python

train_frac    = 0.6
val_frac      = 0.1
learning_rate = 0.001
batch_size    = 32
n_epoch       = 50

```

% SGD optimizer picking the best model on validation data

                             
