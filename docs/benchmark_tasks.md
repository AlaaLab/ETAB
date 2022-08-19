---------------

<p align="center">
  <img width="280" height="160" src="assets/etab_logo.png" />
</p>

<h1 align="center">
    <b> ETAB Benchmark Suite and Model Zoo </b>
</h1>

Our benchmark setup is designed to evaluate general task adaptation approaches. Our notion of "task adaptation" is very general—it includes full representation learning pipelines (i.e., a selection of a model architecture, pre-training task and transfer learning algorithm), or a readily available pre-trained feature representation that is adapted to an echocardiographic task by attaching a task-specific head. This broad notion encapsulates virtually all pre-training approaches, including self-supervised, semi-supervised and supervised learning. 


## Benchmark suite and task categorization

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
  <td>&nbsp;</td>
  <td><s>Interventricular septum thickness estimation</s></td>
    <td><s>Unity</s> (PLAX)</td>
 </tr> 
 <tr>
  <td>&nbsp;</td>
  <td><s>Posterior wall thickness estimation</s></td>
    <td><s>Unity</s> (PLAX)</td>
 </tr>  
 <tr>
 <td colspan="3"> 🟢 &nbsp; <i> View Recognition Tasks </i> </td>
 </tr>
 <tr>
  <td>&nbsp;</td>
  <td>Classifying apical 2- and 4-chamber views</td>
  <td>CAMUS (AP2CH vs. AP4CH)</td>
 </tr>
  <tr>
  <td>&nbsp;</td>
  <td>Classifying parasternal short and long axis views</td>
  <td>TMED (PLAX vs. PSAX)</td>
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



