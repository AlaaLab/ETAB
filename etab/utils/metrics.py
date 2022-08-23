from etab.baselines.models import *
from etab.datasets import *
from etab.utils.visualization import *
from etab.utils.data_tools import *

import numpy as np
import torch
import scipy.stats


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

def dice_coeff(pred, target):
    
    smooth       = 1.
    num          = pred.size(0)
    m1           = pred.view(num, -1).float()  # Flatten
    m2           = target.view(num, -1).float()  # Flatten
    intersection = (m1 * m2).sum().float()

    return (2. * intersection + smooth) / (m1.sum() + m2.sum() + smooth)


def evaluate_model(model, test_loader, task_code="a0"):
    
    metric_ = model.model.evaluate_generator(test_loader)[1][-1]
    
    return metric_