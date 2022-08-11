<p align="center">
  <img width="280" height="160" src="assets/etab_logo.png" />
</p>

<h3 align="center">
    <b> Datasets, Accessibility and Data Processing Tools </b>
</h3>

---------------

The ETAB benchmarks are based on 3 publicly accessible echocardiogram data sets that span different patient cohorts and involve different echo views and annotations. This Section provides a detailed description of the datasets, instructions on how to access each data set, and the data processing tools implemented within the ETAB library.


## Datasets

Below is a high-level description and meta-data for the data sets involved in ETAB.

| Dataset |  Sample size |  Echo views |  Annotations  | 
| :---         |     :---:      |      :---:      |  :--- |
| **EchoNet**   | 10,036 | *AP4CH* | Left ventricle (LV) traces, LV ejection fraction, End-systolic (ES) and End-diastole (ED) frame indexes   |
| **CAMUS**     | 500  | *AP4CH*, *AP2CH* | LV ejection fraction, ES and ED frame indexes, LV epicardium, endocardium and left atrium traces  |
| **TMED**      | 2,341 | *PLAX*, *PSAX* | Aortic Stenosis diagnoses, view annotations  |

**EchoNet data** 

In this data set, introduced in [1], one apical-4 chamber (AP4CH) 2D gray-scale video is extracted from each echo study. A total of 10,036 videos are collected from 10,036 distinct individuals who underwent echocardiography between 2006 and 2018 as part of routine care at a University Hospital. Individuals in the data set were selected at random from hospital records. Along with each video, cardiac function assessments and calculations obtained by a registered sonographer and verified by a level-3 echocardiographer are provided.

**CAMUS data** 

The Cardiac Acquisitions for Multi-structure Ultrasound Segmentation (CAMUS) is an open-access data set from 500 patients, acquired at the University Hospital of St. Etienne (France) [2]. Compared to EchoNet, this data set has a smaller sample size but is more elaborately annotated, hence it serves as an appropriate target data set for a variety of downstream tasks. The data set contains apical two- and four-chamber acquisitions (AP2CH and AP4CH). Half of the population has a left ventricle (LV) ejection fraction lower than 45%, thus being considered at pathological risk. The data set contains full annotation of the left atrium, the endocardium and epicardium borders of the LV, performed by a cardiologist. To identify the beginning and end of each cardiac cycle, End-systolic (ES) and End-diastole (ED) frames within each echo clip are labeled.

**TMED data** 

The Tufts Medical Echocardiogram Dataset (TMED) contains still echocardiogram imagery acquired in the course of routine care from 2015 to 2020 [3]. This data set contains both labeled and unlabeled images—labels include a categorization of views into parasternal long and short axis views (PLAX and PSAX), and diagnostic severity ratings for aortic stenosis (AS). Unlike EchoNet and CAMUS, this data set contains only still images rather than sequences of frames.

## Instructions for dataset access

### The ETAB top-level directory layout

All datasets involved in ETAB are open- or public-access. To run a benchmark experiment, evaluate a pre-trained visual representation using the ETAB score, or implement your own baseline, you need to download the datasets from their original sources. The default data directories in ETAB follow the layout below:

    .
    └── etab
          └── data
                ├── echonet                 # Directory for the EchoNet-Dynamic dataset
                ├── camus                   # Directory for the CAMUS dataset
                └── tmed                    # Directory for the TMED dataset


In each data folder, our scripts expect the content (subfolders and files) to match those of the original data sources. You can customize the data directories by changing the directory variables in the configuration file in the main repo directory as highlighted below:

    .
    └── etab
    ├── docs
    ├── checkpoints
    ├── assets
    ├── config.py                           # Customize your data directories here
    ├── setup.py                 
    └── run_benchmark.py                                             

To set the directories for the EchoNet, CAMUS and TMED data, you can change the values of the **echonet_dir**, **camus_dir** and **tmed_dir** variables in config.py, respectively.

### Downloading the datasets

To download the datasets, please follow the instructions and external links below. 

**EchoNet data** 

*License:*  

To access the EchoNet-Dynamic dataset, please visit this [[link]](https://echonet.github.io/dynamic/) and click on the "Accessing Dataset" button in the main menu. The data resides in the Stanford Artificial Intelligence in Medicine and Imaging (AIMI) Center Shared Datasets Portal (https://stanfordaimi.azurewebsites.net/datasets/834e1cd1-92f7-4268-9daa-d359198b310a). 

**CAMUS data** 

**TMED data**

## Data loaders and processing tools


### References and acknowledgments

If you use ETAB in your research, please acknowledge the authors who contributed by sharing the publicly accessible echocardiography datasets involved in ETAB by citing the following references. 

***EchoNet data*** 

```sh
@inproceedings{ouyang2019echonet,
  title={Echonet-dynamic: a large new cardiac motion video data resource for medical machine learning},
  author={Ouyang, David and He, Bryan and Ghorbani, Amirata and Lungren, Matt P and Ashley, Euan A and Liang, David H and Zou, James Y},
  booktitle={NeurIPS ML4H Workshop: Vancouver, BC, Canada},
  year={2019}
}
```

***CAMUS data*** 

```
@article{leclerc2019deep,
  title={Deep learning for segmentation using an open large-scale dataset in 2D echocardiography},
  author={Leclerc, Sarah and Smistad, Erik and Pedrosa, Joao and {\O}stvik, Andreas and Cervenansky, Frederic and Espinosa, Florian and Espeland, Torvald and Berg, Erik Andreas Rye and Jodoin, Pierre-Marc and Grenier, Thomas and others},
  journal={IEEE transactions on medical imaging},
  volume={38},
  number={9},
  pages={2198--2210},
  year={2019},
  publisher={IEEE}
}
```

***TMED data*** 

```
@inproceedings{huang2021new,
  title={A new semi-supervised learning benchmark for classifying view and diagnosing aortic stenosis from echocardiograms},
  author={Huang, Zhe and Long, Gary and Wessler, Benjamin and Hughes, Michael C},
  booktitle={Machine Learning for Healthcare Conference},
  pages={614--647},
  year={2021},
  organization={PMLR}
}
```
