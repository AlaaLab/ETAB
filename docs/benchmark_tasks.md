---------------

<p align="center">
  <img width="280" height="160" src="assets/etab_logo.png" />
</p>

<h1 align="center">
    <b> ETAB Benchmark Tasks and Model Zoo </b>
</h1>

Currently, the ETAB library is based on three publicly accessible echocardiogram data sets that span different patient cohorts and involve different echocardiographic views and annotations. ETAB is an evolving project that will include more data resources in the future as more datasets become publicly available. This Section provides a detailed description of the datasets, instructions on how to access each dataset, and the data processing tools implemented within the ETAB library.


## Benchmark task categorization and encoding

<div align="center">
<table border="1">
 <tr>
  <td>&nbsp; <b> <div align="center"> Task code        </div> </b> &nbsp;</td>
  <td>&nbsp; <b> <div align="center"> Description      </div> </b> &nbsp;</td>
  <td>&nbsp; <b> <div align="center"> Datasets (Views) </div> </b> &nbsp;</td>
 </tr>
 <tr>
  <td colspan="3"> 🔴 &nbsp; <i> Cardiac Structure Identification Tasks </i> </td>
 </tr>
 <tr>
  <td>&nbsp;</td>
  <td>Segmenting the left ventricle (LV)</td>
  <td>EchoNet (AP4CH), CAMUS (AP2CH and AP4CH)</td>
 </tr>
 <tr>
 <td>&nbsp;</td>
  <td>Segmenting the left atrium (LA)</td>
  <td>CAMUS (AP2CH and AP4CH)</td>
 </tr> 
 <tr>
 <td>&nbsp;</td>
  <td>Segmenting the myocardial wall (MY)</td>
  <td>CAMUS (AP2CH and AP4CH)</td>
 </tr>  
 <tr>
 <td colspan="3"> 🔵 &nbsp; <i> Cardiac Function Estimation Tasks </i> </td>
 </tr>
 <tr>
  <td>&nbsp;</td>
  <td>Estimating LV ejection fraction</td>
  <td>EchoNet (AP4CH), CAMUS (AP2CH and AP4CH)</td>
 </tr>
  <tr>
  <td>&nbsp;</td>
  <td>Classifying end-systole and end-diastole frames</td>
  <td>EchoNet (AP4CH), CAMUS (AP2CH and AP4CH)</td>
 </tr> 
  <tr>
  <td>&nbsp;</td>
  <td><s>Longitudinal strain estimation</s></td>
    <td><s>Unity</s> (AP4CH)</td>
 </tr>   
 <tr>
 <td colspan="3"> 🟢 &nbsp; <i> View Recognition Tasks </i> </td>
 </tr>
 <tr>
  <td>&nbsp;</td>
  <td>Classifying apical 2- and 4-chamber (AP2CH vs. AP4CH) views</td>
  <td>CAMUS</td>
 </tr>
  <tr>
  <td>&nbsp;</td>
  <td>Classifying parasternal short and long axis (PLAX vs. PSAX) views</td>
  <td>TMED</td>
 </tr> 
 <tr>
 <td colspan="3"> 🟡 &nbsp; <i> Clinical Prediction Tasks </i> </td>
 </tr>
 <tr>
  <td>&nbsp;</td>
  <td>Diagnose cardiomyopathy</td>
  <td>EchoNet (AP4CH), CAMUS (AP2CH and AP4CH)</td>
 </tr>
  <tr>
  <td>&nbsp;</td>
  <td>Diagnose aortic stenosis</td>
  <td>TMED (PSAX and PLAX)</td>
 </tr> 
</table>
</div>
  


## ETAB model zoo


## Running a benchmark experiment out-of-the-box


## Implementing a customized model

## References and acknowledgments



