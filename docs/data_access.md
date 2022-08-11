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
| **EchoNet**   | 10,036 | *AP4CH* | Left ventricle (LV) traces, LV ejection fraction, End-systolic (ES) and End-diastole (ED) frames   |
| **CAMUS**     | 500  | *AP4CH*, *AP2CH* | LV ejection fraction, ES and ED frames, LV epicardium, endocardium and left atrium traces  |
| **TMED**      | 2,341 | *PLAX*, *PSAX* | Aortic Stenosis diagnoses, view annotations  |

**EchoNet data** 

In this data set, introduced in [1], one apical-4 chamber (AP4CH) 2D gray-scale video is extracted from each echo study. A total of 10,036 videos are collected from 10,036 distinct individuals who underwent echocardiography between 2006 and 2018 as part of routine care at a University Hospital. Individuals in the data set were selected at random from hospital records. Along with each video, cardiac function assessments and calculations obtained by a registered sonographer and verified by a level-3 echocardiographer are provided.

**CAMUS data** 

The Cardiac Acquisitions for Multi-structure Ultrasound Segmentation (CAMUS) is an open-access data set from 500 patients, acquired at the University Hospital of St. Etienne (France) [2]. Compared to EchoNet, this data set has a smaller sample size but is more elaborately annotated, hence it serves as an appropriate target data set for a variety of downstream tasks. The data set contains apical two- and four-chamber acquisitions (AP2CH and AP4CH). Half of the population has a left ventricle (LV) ejection fraction lower than 45%, thus being considered at pathological risk. The data set contains full annotation of the left atrium, the endocardium and epicardium borders of the LV, performed by a cardiologist. To identify the beginning and end of each cardiac cycle, End-systolic (ES) and End-diastole (ED) frames within each echo clip are labeled.

**TMED data** 

The Tufts Medical Echocardiogram Dataset (TMED) contains still echocardiogram imagery acquired in the course of routine care from 2015 to 2020 [3]. This data set contains both labeled and unlabeled images—labels include a categorization of views into parasternal long and short axis views (PLAX and PSAX), and diagnostic severity ratings for aortic stenosis (AS). Unlike EchoNet and CA83 MUS, this data set contains only still images rather than sequences of frames.

## Instructions for dataset access


## Data loaders and processing tools


### References and acknowledgments
