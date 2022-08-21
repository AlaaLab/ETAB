---------------

<p align="center">
  <img width="280" height="160" src="assets/etab_logo.png" />
</p>

<h1 align="center">
    <b> The ETAB Evaluation Protocol </b>
</h1>

In many cases, we might be interested in evaluating a visual representation pre-trained on an external data set with respect to their ability to capture all relevant features in echocardiograms. These pre-trained representations might have been trained on private echocardiogram data, data for other cardiac imaging modalities, or even a general visual representation pre-trained on non-medical data such as ImageNet. The ETAB evaluation protocol uses the suite of benchmark tasks listed in the previous Section to evaluate the usefulness of any given (pre-trained) visual representation for a wide variety of common tasks in echocardiography. In this Section, we describe the ETAB evaluation protocol and provide code snippets illustrating how the user can compute the "ETAB score" for a pre-trained backbone representation.


## Description of the evaluation protocol

The evaluation protocol is meant to assess how well does a given pre-trained backbone representation perform on the ETAB benchmark tasks. Here, we freeze the backbone representation and only tune the task-specific head for each individual task. The output of the process is an *ETAB score*, which is a number in [0,1] that quantifies the quality of the pre-trained representation. A schematic depiction of the protocol along with a mathematical description are given below.

<p align="center">
  <img width="488" height="320" src="assets/ETABscore.png" />
</p>

Let $\mathcal{K} = \{1, \ldots, K\}$ be the target task categories, and let $\mathcal{T}\_k = \{t\_{1,k}, \ldots, t\_{T\_k,k}\}$ be the tasks within category $k \in \mathcal{K}$. Let $\mathcal{D}\_{t, k}$ be the target data set associated with the $t$-th task within the $k$-th category. A given adaptation model $\mathcal{M}$ is provided with $n$ samples of the target data set $\mathcal{D}^n\_{t, k} = \{(X^i\_{t, k}, Y^i\_{t, k})\}^n\_{i=1}$, and outputs an adapted target model $\mathcal{M}(\mathcal{D}^n\_{t, k})$. Let $\mathcal{E}\_{t,k}$ be the evaluation metric used to assess the performance of the target model; we assume that $\mathcal{E}\_{t,k}$ takes on values in $[0,1]$. The ETAB score for the adaptation model $\mathcal{M}$ is thus defined as: 

$\mbox{ETAB}\_k^n(\mathcal{M}) \triangleq \mathbb{E}\_{t \sim P\_{\mathcal{T}\_k}} \mathcal{E}\_{t,k}\left\[\,\mathcal{M}(\mathcal{D}^n\_{t, k})\,\right\]$

$\mbox{ETAB}^n(\mathcal{M}) \triangleq \mathbb{E}\_{k \sim P_\mathcal{K}} \mbox{ETAB}\_k^n(\mathcal{M}).$

The score computation procedure is implemented by looping over all the benchmark tasks listed in the previous Section, and then computed a weighted average of the performance of a given backbone representation attached to the task-specific heads. 


## Computing the ETAB score

For a given backbone representation, the ETAB score can be computed using the *ETABscore()* function in the *etab.scores* module using the simple API demonstrated below:

```python
from etab.scores import ETABscore
from torchvision.models import resnet50

weight_dict = dict({"a": 0.5, "b": 0.3, 
                   "c": 0.1, "d": 0.1})
                   
backbone    = resnet50(weights="IMAGENET1K_V1")

etab_score = ETABscore(backbone=backbone, task_weights=weight_dict)
```
Here, we evaluate the ETAB score for a ResNet-50 backbone pre-trained on the ImageNet-1K dataset. The weight dictionary *weight_dict* dictates the relevant importance of the different task categories described in the previous section (Categories 🔴 a, 🔵 b, 🟢 c and 🟡 d). Currently, the ETAB score can be computed for the backbone representations listed in the previous Section. You can load any pre-trained weights into these representations prior to computing the score. 

The *ETABscore()* function also enables a customized weighting of prespecified set of benchmark tasks by specifying the benchmark codes as dictionary keys as shown below:
```python
weight_dict = dict({"a0-A4-E": 0.5, "a0-A4-C": 0.3, "a0-A2-C": 0.2})
               
etab_score = ETABscore(backbone=backbone, task_weights=weight_dict)
```
The output of the *ETABscore()* function is a tuple of the form *etab_score = (Average ETAB score, 95\% confidence interval)*. The error bars are obtained by testing the backbone across each benchmark task through a number of different train/test splits. The number of training folds can be changed by setting the *n_fold* argument of *ETABscore()*, and the default value of *n_fold* is 5.








