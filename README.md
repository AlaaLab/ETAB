<h3 align="center">
    <b> ETAB: A Benchmark Suite for Visual Representation Learning in Echocardiography </b>
</h3>

---------------

[![Python 3.6+](https://img.shields.io/badge/Platform-Python%203.6-blue.svg)](https://www.python.org/)
[![PyTorch 1.1.0](https://img.shields.io/badge/Implementation-Pytorch-brightgreen.svg)](https://pytorch.org/)

The echocardiographic task adaptation benchmark (ETAB) library contains a suite of standardized benchmarks that can be used to evaluate visual representations of cardiac ultrasound (echocardiogram) data with respect to various clinically-relevant tasks using publicly accessible data sets. The ETAB library provides an easy-to-use API for loading various echocardiographic data sets and implementing new algorithms, a unified evaluation protocol for echocardiographic representations and a set of pre-trained models for echocardiograms.

---------------
#### Overview

Echocardiography is one of the most commonly used non-invasive imaging techniques for assessing cardiac function, examining heart anatomy and diagnosing cardiovascular diseases. An echo study is an ultrasound of the heart acquired by a cardiac sonographer through a transducer device—different acquisition angles by which the device is placed relative to the patient's heart provide different *views* of the heart anatomy. Echocardiograms inform cardiologists, surgeons, oncologists and emergency physicians on clinical decisions pertaining to treatment management and surgical planning. Because of the central role it plays in cardiovascular medicine, there has been a significant interest in applying deep learning-based computer vision models to echocardiograms, with the ultimate goal of automating cardiac evaluation, reducing variance and improving reproducibility in interpreting echocardiograms, and predicting patient-specific clinical outcomes.

---------------

#### [Datasets, accessibility and dataset tools](documentation/data_access.md)

#### [Benchmark tasks](documentation/benchmark_tasks.md)

#### [The ETAB evaluation protocol](documentation/benchmark_tasks.md)

#### [Implementing your own baselines](documentation/implementing_baselines.md)

#### [Leaderboard and benchmark results](documentation/leaderboard.md)

