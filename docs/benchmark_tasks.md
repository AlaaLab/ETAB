---------------

<p align="center">
  <img width="280" height="160" src="assets/etab_logo.png" />
</p>

<h1 align="center">
    <b> ETAB Benchmark Suite and Model Zoo </b>
</h1>

The ETAB benchmark suite encapsulates a diverse set of tasks that are meant to test the quality of visual representations of echocardiograms with respect to different downstream setups of interest across different datasets. The benchmark tasks fall in four different catgeories: 🔴 *cardiac structure identification* tasks where the goal is to automatically identify anatomical regions of interest, 🔵 *cardiac function estimation* tasks where the goal is to evaluate cardiac hemodynamics and left ventricle measurements, 🟢 *view recognition tasks* where the goal is to automate view annotations for echocardiography clips, and 🟡 *clinical prediction tasks* where the goal is to predict clinical outcomes or issue diagnoses based on observed echocardiograms. Combinations of these tasks constitute adaptation benchmarks that can be used to evaluate transferrability of features across views, data sets and annotations. In this Section, we provide an overview of the ETAB benchmark suite and the supported built-in vision models, along with code snippets and demo notebooks illustrating how users can run a benchmark experiment out-of-the-box. 


## Benchmark task categorization and encoding

<div align="center">
<table border="1">
  <tr>
  <td colspan="3"> <div align="center"> <b> Benchmark code </b> </div> </td>
 </tr>
 <tr>
  <td> <i> <div align="center"> Dataset code  </div> </i> </td>
  <td> <i> <div align="center"> View code     </div> </i> </td>
  <td> <i> <div align="center"> Task code     </div> </i> </td>
 </tr>
</table>
</div>

<div align="center">
<table border="1">
  <tr>
  <td colspan="4"> <div align="center"> <b> Dataset code </b> </div> </td>
 </tr>
 <tr>
  <td> <i> <div align="center"> EchoNet  </div> </i> </td>
  <td>     <div align="center"> E               </i> </td>
  <td> <i> <div align="center"> CAMUS    </div> </i>   </td>
  <td>     <div align="center"> C               </i> </td> 
 </tr>
 <tr>
  <td> <i> <div align="center"> TMED   </div> </i> </td>
  <td>     <div align="center"> T             </i> </td>
  <td> <i> <div align="center"> Unity  </div> </i> </td>
  <td>     <div align="center"> U             </i> </td>
 </tr> 
</table>
</div>

<div align="center">
<table border="1">
  <tr>
  <td colspan="4"> <div align="center"> <b> View code </b> </div> </td>
 </tr>
 <tr>
  <td> <i> <div align="center"> APnCH  </div> </i> </td>
  <td>     <div align="center"> Apical n-chamber  </i> </td>
 </tr>
 <tr>
  <td> <i> <div align="center"> PLAX  </div> </i> </td>
  <td>     <div align="center"> E               </i> </td>
 </tr>
 <tr>
  <td> <i> <div align="center"> PSAX  </div> </i> </td>
  <td>     <div align="center"> E               </i> </td>
 </tr> 

</table>
</div>

   
<div align="center">
<table border="1">
 <tr>
  <td>&nbsp; <b> <div align="center"> Task code        </div> </b> &nbsp;</td>
  <td>&nbsp; <b> <div align="center"> Description      </div> </b> &nbsp;</td>
  <td>&nbsp; <b> <div align="center"> Datasets (Views) </div> </b> &nbsp;</td>
 </tr>
 <tr>
  <td colspan="3"> 🔴 &nbsp; <i> Cardiac Structure Identification Tasks </i> <b> (Category: a) </b> </td>
 </tr>
 <tr>
  <td><b> 0 </b></td>
  <td>Segmenting the left ventricle (LV)</td>
  <td>EchoNet (AP4CH), CAMUS (AP2CH and AP4CH)</td>
 </tr>
 <tr>
 <td><b> 1 </b></td>
  <td>Segmenting the left atrium (LA)</td>
  <td>CAMUS (AP2CH and AP4CH)</td>
 </tr> 
 <tr>
 <td><b> 2 </b></td>
  <td>Segmenting the myocardial wall (MY)</td>
  <td>CAMUS (AP2CH and AP4CH)</td>
 </tr>  
 <tr>
 <td colspan="3"> 🔵 &nbsp; <i> Cardiac Function Estimation Tasks </i> <b> (Category: b) </b> </td>
 </tr>
 <tr>
  <td><b> 0 </b></td>
  <td>Estimating LV ejection fraction</td>
  <td>EchoNet (AP4CH), CAMUS (AP2CH and AP4CH)</td>
 </tr>
  <tr>
  <td><b> 1 </b></td>
  <td>Classifying end-systole and end-diastole frames</td>
  <td>EchoNet (AP4CH), CAMUS (AP2CH and AP4CH)</td>
 </tr> 
  <tr>
  <td><b> 2 </b></td>
  <td><s>Longitudinal strain estimation</s></td>
    <td><s>Unity</s> (AP4CH)</td>
 </tr>
 <tr>
  <td><b> 3 </b></td>
  <td><s>Interventricular septum thickness estimation</s></td>
    <td><s>Unity</s> (PLAX)</td>
 </tr> 
 <tr>
  <td><b> 4 </b></td>
  <td><s>Posterior wall thickness estimation</s></td>
    <td><s>Unity</s> (PLAX)</td>
 </tr>  
 <tr>
 <td colspan="3"> 🟢 &nbsp; <i> View Recognition Tasks </i> <b> (Category: c) </b> </td>
 </tr>
 <tr>
  <td><b> 0 </b></td>
  <td>Classifying apical 2- and 4-chamber views</td>
  <td>CAMUS (AP2CH vs. AP4CH)</td>
 </tr>
  <tr>
  <td><b> 1 </b></td>
  <td>Classifying parasternal short and long axis views</td>
  <td>TMED (PLAX vs. PSAX)</td>
 </tr> 
 <tr>
  <td><b> 2 </b></td>
  <td><s>Classifying all apical and parasternal views</s></td>
  <td><s>Unity</s> (AP2CH vs. AP3CH vs. AP4CH vs. AP5CH vs. PLAX vs. PSAX)</td>
 </tr>  
 <tr>
 <td colspan="3"> 🟡 &nbsp; <i> Clinical Prediction Tasks </i> <b> (Category: d) </b> </td>
 </tr>
 <tr>
  <td><b> 0 </b></td>
  <td>Diagnose cardiomyopathy</td>
  <td>EchoNet (AP4CH), CAMUS (AP2CH and AP4CH)</td>
 </tr>
  <tr>
  <td><b> 1 </b></td>
  <td>Diagnose aortic stenosis</td>
  <td>TMED (PSAX and PLAX)</td>
 </tr> 
</table>
</div>
  


## ETAB model zoo


## Running a benchmark experiment out-of-the-box


## Implementing a customized model

## References and acknowledgments



