---------------

<p align="center">
  <img width="280" height="160" src="assets/etab_logo.png" />
</p>

<h1 align="center">
    <b> Datasets, Accessibility and Data Processing Tools </b>
</h1>

Currently, the ETAB library is based on three publicly accessible echocardiogram data sets that span different patient cohorts and involve different echocardiographic views and annotations. ETAB is an evolving project that will include more data resources in the future as more datasets become publicly available. This Section provides a detailed description of the datasets, instructions on how to access each dataset, and the data processing tools implemented within the ETAB library.


## Datasets

Below is a high-level description and meta-data for the data sets involved in ETAB.

| Dataset |  Sample size |  Echo views |  Annotations  | 
| :---         |     :---:      |      :---:      |  :--- |
| **EchoNet**   | 10,036 | *AP4CH* | Left ventricle (LV) traces, LV ejection fraction, End-systolic (ES) and End-diastole (ED) frame indexes   |
| **CAMUS**     | 500  | *AP4CH*, *AP2CH* | LV ejection fraction, ES and ED frame indexes, LV epicardium, endocardium and left atrium traces  |
| **TMED**      | 2,341 | *PLAX*, *PSAX* | Aortic Stenosis diagnoses, view annotations  |

**EchoNet data** 

In this data set, one apical-4 chamber (AP4CH) 2D gray-scale video is extracted from each echo study. A total of 10,036 videos are collected from 10,036 distinct individuals who underwent echocardiography between 2006 and 2018 as part of routine care at a University Hospital. Individuals in the data set were selected at random from hospital records. Along with each video, cardiac function assessments and calculations obtained by a registered sonographer and verified by a level-3 echocardiographer are provided.

**CAMUS data** 

The Cardiac Acquisitions for Multi-structure Ultrasound Segmentation (CAMUS) is an open-access data set from 500 patients, acquired at the University Hospital of St. Etienne (France). Compared to EchoNet, this data set has a smaller sample size but is more elaborately annotated, hence it serves as an appropriate target data set for a variety of downstream tasks. The data set contains apical two- and four-chamber acquisitions (AP2CH and AP4CH). Half of the population has a left ventricle (LV) ejection fraction lower than 45%, thus being considered at pathological risk. The data set contains full annotation of the left atrium, the endocardium and epicardium borders of the LV, performed by a cardiologist. To identify the beginning and end of each cardiac cycle, End-systolic (ES) and End-diastole (ED) frames within each echo clip are labeled.

**TMED data** 

The Tufts Medical Echocardiogram Dataset (TMED) contains still echocardiogram imagery acquired in the course of routine care from 2015 to 2020. This data set contains both labeled and unlabeled images—labels include a categorization of views into parasternal long and short axis views (PLAX and PSAX), and diagnostic severity ratings for aortic stenosis (AS). Unlike EchoNet and CAMUS, this data set contains only still images rather than sequences of frames.

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

To download the datasets, please follow the instructions and external links below. Please note that the ETAB library provides a standardized API for loading and processing all datasets for the sake of model development and training, but it does not alter, distribute or directly share the datasets. Please make sure to follow the terms of the respective *Research Use Agreements* for all datasets upon access.  

**EchoNet data** 

*License:* [Stanford University EchoNet-Dynamic Dataset Research Use Agreement](https://stanfordaimi.azurewebsites.net/datasets/834e1cd1-92f7-4268-9daa-d359198b310a) 

To access the EchoNet-Dynamic dataset, please visit this [Link](https://echonet.github.io/dynamic/), click on the "Accessing Dataset" button in the main menu, and follow the instructions therein. The data resides in the Stanford Artificial Intelligence in Medicine and Imaging (AIMI) Center Shared Datasets [Portal](https://stanfordaimi.azurewebsites.net/datasets/834e1cd1-92f7-4268-9daa-d359198b310a). The data folder size is 7.04 GB. The downloaded folders should be located in the "echonet" folder according to the directory layout above (or a customized directory specified in config.py). The contents of the "echonet" folder should follow the layout below.

    .
    └── echonet
           ├── Videos                 # Directory for the echocardiography clips
           ├── VolumeTracings.csv     # Directory for the left ventricle tracings
           └── FileList.csv           # Directory for the meta-data


**CAMUS data** 

*License:* Please refer to the CAMUS [online platform](https://www.creatis.insa-lyon.fr/Challenge/camus/).

The CAMUS dataset is publicly accessible, and is held and maintained within the CAMUS [online platform](https://www.creatis.insa-lyon.fr/Challenge/camus/). The data can be directly downloaded through the online platform upon registering. The "camus" data folder should be structured in a similar manner to the original data folder on the online platform; the directoty should follow the layout below: 

    .
    └── camus
           ├── training          # Folder containing data for training echo clips
           └── testing           # Folder containing data for testing echo clips



**TMED data**

*License:* [The TMED Health Data License](https://tmed.cs.tufts.edu/data_license.html)

To access the Tufts Medical Echocardiogram Dataset (TMED) dataset, please visit the official TMED [website](https://tmed.cs.tufts.edu/), click on the [Data Access](https://tmed.cs.tufts.edu/data_access.html) button in the main menu, and follow the instructions therein. The downloaded folders should be located in the "tmed" folder according to the directory layout above (or a customized directory specified in config.py). The contents of "tmed" folder should follow the layout below:

    .
    └── tmed
          ├── labels_per_image.csv
          ├── TMED2_fold0_labeledpart.csv
          ├── TMED2_fold1_labeledpart.csv
          └── TMED2_fold2_labeledpart.csv

Please note that ETAB operates on the labeled samples of TMED only. You do not need to include the unlabeled data in the tmed folder to run the ETAB benchmarks.


## Data loaders and processing tools ([**demo notebook**](https://github.com/ahmedmalaa/ETAB/blob/main/notebooks/Demo%201%20-%20ETAB%20Data%20Loading%20and%20Processing%20Tools.ipynb))

The ETAB library provides a unified API for loading echocardiography datasets and pre-processing the data for model development. Below is an overview of the ETAB data structures and functionalities. Detailed examples and code snippets for loading and processing echocardiography datasets are provided in this [**demo notebook**](https://github.com/ahmedmalaa/ETAB/blob/main/notebooks/Demo%201%20-%20ETAB%20Data%20Loading%20and%20Processing%20Tools.ipynb).

### The *ETAB_dataset* class

Each dataset is an instantiation of the *ETAB_dataset* class, which contains common attributes and a unified API for all data processing functionalities. A code snippet for creating an instance of the *ETAB_dataset* class is demonstrated below.

```
import etab

echonet = etab.ETAB_dataset(name="echonet",
                            target="EF",
                            view="A4CH",
                            video=False,
                            normalize=True,
                            frame_l=224,
                            frame_w=224,
                            clip_l=16, 
                            fps=50,
                            padding=None)
```

You can craft a dataset that suits the modeling problem of interest by customizing the values for the *ETAB_dataset* class attributes. The meaning of all class attributes are listed below.

- **name:** The source of the data to be loaded. Current options include "echonet", "camus" and "tmed".
- **target:** The labels associated with each patient. Options include "EF", "LV_seg", "LA_seg", "MY_seg", "ES/ED", "view", "CM", "AS".
- **view:** The echocardiographic views for the loaded data. Options include "AP4CH", "AP2CH", "PLAX" and "PSAX".
- **video:** A boolean indicating whether data should be loaded as a sequence of frames for each patient. Setting this to "False" means that data will include only the first frame in each clip.
- **normalize:** A boolean indicating whether pixel values should be normalized using the ImageNet mean and variance.
- **frame_l, frame_w and clip_l:** Frame length and width (in terms of the number of pixels), and clip length in terms of number of frames.
- **fps:** Sampling rate for the loaded video. 
- **padding:** Add zeros to clips that are shorter than *clip_l*.


### Data tools and functionalities

Having instantiated an *ETAB_dataset* class, we can craft an echocardiography data set with the options specified in the class instantiation by calling the *load_data* method as follows:

```
echonet.load_data(n_clips=100, random=False)
```
This command will load 100 clips into the *.data* attribute of *echonet*. The data will be loaded from EchoNet in order if *random* is set to False, and will be randomly sampled otherwise. Each data point will be associated with the label specified in the class options used within the instantiating command above. We can visualize the data for patient number *index* using the *plot_segment* function as follows:

```
echo_image = echonet.data[index][0]
LV_segment = echonet.data[index][1][0]
plot_segment(echo_image, LV_segment, overlay=True, color="r")
```
This last command should display the following plot for *index=65*

<p> 
  <img width="160" height="160" src="assets/echonet_LV.png" /> 
</p>

Further example on data with traces of the left ventricle, left atrium and myocardial wall from the CAMUS dataset are shown below. The code for reproducing these plots is provided in the [**demo notebook**](https://github.com/ahmedmalaa/ETAB/blob/main/notebooks/Demo%201%20-%20ETAB%20Data%20Loading%20and%20Processing%20Tools.ipynb).

<p> 
  <img width="160" height="160" src="assets/camus_LV.png" /> 
  <img width="160" height="160" src="assets/camus_LA.png" /> 
  <img width="160" height="160" src="assets/camus_MY.png" /> 
</p>

Now let us create a new instance of EchoNet but with a different data structure. This time, we create a video dataset where the labels correspond to the LV ejection fraction. To create such an instance, we supply the class with the set of options and attributes below.

```
echonet = ETAB_dataset(name="echonet",
                       target="EF", 
                       view="A4",
                       video=False,
                       normalize=True,
                       frame_l=224,
                       frame_w=224,
                       clip_l=16, 
                       fps=50,
                       padding=None)
```

To animate an echocardiographic video and save it as a gif, you can use the *create_echo_clip* function as follows

```
create_echo_clip(echonet.data[0][0], "demo_clip")
```

This will save the gif file below in a folder named "echo_clips" in the current directoty...

<p> 
  <img width="160" height="160" src="assets/demo_clip.gif" /> 
</p>


Training and testing data can be loaded using the **train_test_split** function in **etab.utils.data_tools** as follows:

```
from etab.utils.data_tools import train_test_split

train_data, val_data, test_data = train_test_split(echonet, train_frac=0.5, val_frac=0.1, random=True)
```

In the above, the variables *train_data*, *val_data*, and *test_data* are iterables that contain the training/validation/testing splits. Each data point is a tuple where the first element (e.g., train_data[index][0]) conrains a *frame_l x frame_w* image (or a list of images of length *clip_l* if *video* is True), and the second element (e.g., train_data[index][1]) conrains the label. The label can be an image (for segmentation tasks), a real-valued target (for regression tasks) or a binary/discrete label (for classification tasks). 


## References and acknowledgments

If you use ETAB in your research, please acknowledge the authors who contributed by sharing the publicly accessible echocardiography datasets. You can credit the datasets' authors by citing the following references. 

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
