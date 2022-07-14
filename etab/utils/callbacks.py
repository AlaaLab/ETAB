import os
import tarfile
import urllib.request
import numpy as np

from poutyne import set_seeds, Model, ModelCheckpoint, CSVLogger, Experiment

import pickle

set_seeds(42)



def init_callbacks(benchmark_task_code):

    save_base_dir = 'checkpoints'
    save_path     = os.path.join(save_base_dir, benchmark_task_code)

    # Creating saving directory
    os.makedirs(save_path, exist_ok=True)

    callbacks = [
        # Save the latest weights to be able to continue the optimization at the end for more epochs.
        ModelCheckpoint(os.path.join(save_path, 'last_weights.ckpt')),

        # Save the weights in a new file when the current model is better than all previous models.
        ModelCheckpoint(os.path.join(save_path, 'best_weight.ckpt'),
                        save_best_only=True, restore_best=True, verbose=True),

        # Save the losses for each epoch in a TSV.
        CSVLogger(os.path.join(save_path, 'log.tsv'), separator='\t'),
    ]
    
    return callbacks