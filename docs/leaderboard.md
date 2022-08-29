---------------

<p align="center">
  <img width="280" height="160" src="assets/etab_logo.png" />
</p>

<h1 align="center">
    <b> Leaderboard and Benchmark Results </b>
</h1>

## ETAB Leaderboard

The ETAB leaderboard keeps track of the best performing backbone architectures with respect to benchmark echocardiographic tasks. 

| **Latest update**  | August 28, 2022 |
| ------------- | ------------- |
| **Current status**  | ▶ **Running** [🔴 Cardiac structure identification benchmarks](https://github.com/ahmedmalaa/ETAB/blob/main/docs/benchmark_tasks.md#benchmark-task-categorization-and-encoding)  |
| **Progress** | **5** out of **19** benchmark tasks completed ![26%](https://progress-bar.dev/26) <br/> **10** out of **14** baseline models evaluated ![71%](https://progress-bar.dev/71)|

<div align="center">
<table border="1">
 <tr>
  <td> <b> <div align="center"> Ranking                              </div> </b> </td>
  <td> <b> <div align="center"> Backbone                             </div> </b> </td>
  <td> <b> <div align="center"> # Parameters                         </div> </b> </td>
  <td> <b> <div align="center"> ETAB score                           </div> </b> </td>
  <td> <b> <div align="center"> Task-specific performance breakdown </div> </b> </td>
  <td> <b> <div align="center"> Pre-trained weights                  </div> </b> </td>
 </tr>
  
 <tr>
  <td> <b> <div align="center"> 1 </div> </b> </td>
  <td> <div align="center"> MobileNet-V2 <br> (ImageNet-1K weights) </div> </td>
  <td> <div align="center"> 3.5M </div> </td>
  <td> <div align="center"> 0.783 </div> </td>
  <td> <details>
  <summary><b>Score breakdown</b> (click to expand)</summary>
  &nbsp;
  <ul>
    <li> 🔴 a0-A4-E: 0.825 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a0-A4-C: 0.841 | weight: 0.2</li>
    &nbsp;
    <li> 🔴 a0-A2-C: 0.840 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A4-C: 0.709 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A2-C: 0.698 | weight: 0.2</li> 
  </ul>

</details> </td> 
  <td> <div align="center"> <a href="https://pytorch.org/vision/stable/models/generated/torchvision.models.mobilenet_v2.html#torchvision.models.MobileNet_V2_Weights">Download</a> </div> </td> 
 </tr>  

 <tr>
  <td> <b> <div align="center"> 2 </div> </b> </td>
  <td> <div align="center"> ResNet-50 <br> (Fully finetuned) </div> </td>
  <td> <div align="center"> 23M </div> </td>
  <td> <div align="center"> 0.769 </div> </td>
  <td> 
    <details>
  <summary><b>Score breakdown</b> (click to expand)</summary>
  &nbsp;
  <ul>
    <li> 🔴 a0-A4-E: 0.855 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a0-A4-C: 0.820 | weight: 0.2</li>
    &nbsp;
    <li> 🔴 a0-A2-C: 0.822 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A4-C: 0.693 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A2-C: 0.656 | weight: 0.2</li> 
  </ul>

</details> </td> 
  <td> <div align="center"> <a href="https://pytorch.org/vision/main/models/generated/torchvision.models.resnet50.html">Download</a> </div> </td> 
 </tr>

   <tr>
  <td> <b> <div align="center"> 3 </div> </b> </td>
  <td> <div align="center"> MobileNet-V3-Large <br> (ImageNet-1K weights) </div> </td>
  <td> <div align="center"> 5.5M </div> </td>
  <td> <div align="center"> 0.749 </div> </td>
  <td> <details>
  <summary><b>Score breakdown</b> (click to expand)</summary>
  &nbsp;
  <ul>
    <li> 🔴 a0-A4-E: 0.838 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a0-A4-C: 0.805 | weight: 0.2</li>
    &nbsp;
    <li> 🔴 a0-A2-C: 0.808 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A4-C: 0.656 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A2-C: 0.636 | weight: 0.2</li> 
  </ul>

</details> </td>  </td> 
  <td> <div align="center"> <a href="https://pytorch.org/vision/stable/models/generated/torchvision.models.mobilenet_v3_large.html#torchvision.models.MobileNet_V3_Large_Weights">Download</a> </div> </td> 
 </tr> 
  
  
  
  <tr>
  <td> <b> <div align="center"> 4 </div> </b> </td>
  <td> <div align="center"> ResNet-18 <br> (ImageNet-1K weights) </div> </td>
  <td> <div align="center"> 11M </div> </td>
  <td> <div align="center"> 0.702 </div> </td>
  <td>  <details>
  <summary><b>Score breakdown</b> (click to expand)</summary>
  &nbsp;
  <ul>
    <li> 🔴 a0-A4-E: 0.776 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a0-A4-C: 0.764 | weight: 0.2</li>
    &nbsp;
    <li> 🔴 a0-A2-C: 0.753 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A4-C: 0.605 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A2-C: 0.609 | weight: 0.2</li> 
  </ul>
</details> </td> 
  <td> <div align="center"> <a href="https://pytorch.org/vision/main/models/generated/torchvision.models.resnet18.html">Download</a> </div> </td> 
 </tr> 
  
  
 <tr>
  <td> <b> <div align="center"> 5 </div> </b> </td>
  <td> <div align="center"> ResNet-34 <br> (ImageNet-1K weights) </div> </td>
  <td> <div align="center"> 63M </div> </td>
  <td> <div align="center"> 0.699 </div> </td>
  <td>     <details>
  <summary><b>Score breakdown</b> (click to expand)</summary>
  &nbsp;
  <ul>
    <li> 🔴 a0-A4-E: 0.774 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a0-A4-C: 0.734 | weight: 0.2</li>
    &nbsp;
    <li> 🔴 a0-A2-C: 0.734 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A4-C: 0.643 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A2-C: 0.611 | weight: 0.2</li> 
  </ul>

</details> </td> 
  <td> <div align="center"> <a href="https://pytorch.org/vision/main/models/generated/torchvision.models.resnet34.html">Download</a> </div> </td> 
 </tr>
  
 <tr>
  <td> <b> <div align="center"> 6 </div> </b> </td>
  <td> <div align="center"> PoolFormer-S24 <br> (ImageNet-1K weights) </div> </td>
  <td> <div align="center"> 21M </div> </td>
  <td> <div align="center"> 0.692 </div> </td>
  <td> <details>
  <summary><b>Score breakdown</b> (click to expand)</summary>
  &nbsp;
  <ul>
    <li> 🔴 a0-A4-E: 0.719 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a0-A4-C: 0.772 | weight: 0.2</li>
    &nbsp;
    <li> 🔴 a0-A2-C: 0.754 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A4-C: 0.597 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A2-C: 0.615 | weight: 0.2</li> 
  </ul>

</details> </td> 
  <td> <div align="center"> <a href="https://huggingface.co/sail/poolformer_s24">Download</a> </div> </td> 
</tr>   
  
 <tr>
  <td> <b> <div align="center"> 7 </div> </b> </td>
  <td> <div align="center"> MiT-B2 <br> (fully tuned) </div> </td>
  <td> <div align="center"> 25M </div> </td>
  <td> <div align="center"> 0.691 </div> </td>
  <td> <details>
  <summary><b>Score breakdown</b> (click to expand)</summary>
  &nbsp;
  <ul>
    <li> 🔴 a0-A4-E: 0.749 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a0-A4-C: 0.748 | weight: 0.2</li>
    &nbsp;
    <li> 🔴 a0-A2-C: 0.738 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A4-C: 0.595 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A2-C: 0.626 | weight: 0.2</li> 
  </ul>

</details></td> 
  <td> <div align="center"> <a href="https://huggingface.co/docs/transformers/model_doc/segformer">Download</a> </div> </td> 
</tr>  
  
  
  
  <tr>
  <td> <b> <div align="center"> 8 </div> </b> </td>
  <td> <div align="center"> ResNet-50 <br> (ImageNet-1K weights) </div> </td>
  <td> <div align="center"> 23M </div> </td>
  <td> <div align="center"> 0.689 </div> </td>
  <td> <details>
  <summary><b>Score breakdown</b> (click to expand)</summary>
  &nbsp;
  <ul>
    <li> 🔴 a0-A4-E: 0.787 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a0-A4-C: 0.738 | weight: 0.2</li>
    &nbsp;
    <li> 🔴 a0-A2-C: 0.719 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A4-C: 0.604 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A2-C: 0.597 | weight: 0.2</li> 
  </ul>

</details> </td> 
  <td> <div align="center"> <a href="https://pytorch.org/vision/main/models/generated/torchvision.models.resnet50.html">Download</a> </div> </td> 
 </tr> 
  
 <tr>
  <td> <b> <div align="center"> 9 </div> </b> </td>
  <td> <div align="center"> MiT-B2 <br> (ImageNet-1K weights) </div> </td>
  <td> <div align="center"> 25M </div> </td>
  <td> <div align="center"> 0.653 </div> </td>
  <td> <details>
  <summary><b>Score breakdown</b> (click to expand)</summary>
  &nbsp;
  <ul>
    <li> 🔴 a0-A4-E: 0.674 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a0-A4-C: 0.709 | weight: 0.2</li>
    &nbsp;
    <li> 🔴 a0-A2-C: 0.708 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A4-C: 0.570 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A2-C: 0.604 | weight: 0.2</li> 
  </ul>

</details></td> 
  <td> <div align="center"> <a href="https://huggingface.co/docs/transformers/model_doc/segformer">Download</a> </div> </td> 
</tr> 
  
  <tr>
  <td> <b> <div align="center"> 10 </div> </b> </td>
  <td> <div align="center"> ConvNext-Base <br> (fully tuned) </div> </td>
  <td> <div align="center"> 8M </div> </td>
  <td> <div align="center"> 0.647 </div> </td>
  <td> <details>
  <summary><b>Score breakdown</b> (click to expand)</summary>
  &nbsp;
  <ul>
    <li> 🔴 a0-A4-E: 0.801 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a0-A4-C: 0.647 | weight: 0.2</li>
    &nbsp;
    <li> 🔴 a0-A2-C: 0.699 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A4-C: 0.550 | weight: 0.2</li> 
    &nbsp;
    <li> 🔴 a1-A2-C: 0.539 | weight: 0.2</li> 
  </ul>

</details> </td> 
  <td> <div align="center"> <a href="https://pytorch.org/vision/stable/models/generated/torchvision.models.convnext_base.html#torchvision.models.convnext_base">Download</a> </div> </td> 
</tr>  
    
  
 <tr>
  <td> <b> <div align="center"> 11 </div> </b> </td>
  <td> <div align="center"> DenseNet-121 <br> (ImageNet-1K weights) </div> </td>
  <td> <div align="center"> 8M </div> </td>
  <td> <div align="center"> --- </div> </td>
  <td> --- </td> 
  <td> <div align="center"> <a href="https://pytorch.org/vision/stable/models/generated/torchvision.models.densenet121.html#torchvision.models.DenseNet121_Weights">Download</a> </div> </td> 
 </tr> 

  
  <tr>
  <td> <b> <div align="center"> 12 </div> </b> </td>
  <td> <div align="center"> ResNeXt-50-32x4d <br> (ImageNet-1K weights) </div> </td>
  <td> <div align="center"> 25M </div> </td>
  <td> <div align="center"> --- </div> </td>
  <td> --- </td> 
  <td> <div align="center"> <a href="https://pytorch.org/vision/stable/models/generated/torchvision.models.resnext50_32x4d.html#torchvision.models.ResNeXt50_32X4D_Weights">Download</a> </div> </td> 
 </tr>  

  <tr>
  <td> <b> <div align="center"> 13 </div> </b> </td>
  <td> <div align="center"> Inception_V3 <br> (ImageNet-1K weights) </div> </td>
  <td> <div align="center"> 27M </div> </td>
  <td> <div align="center"> --- </div> </td>
  <td> --- </td> 
  <td> <div align="center"> <a href="https://pytorch.org/vision/stable/models/generated/torchvision.models.inception_v3.html#torchvision.models.Inception_V3_Weights">Download</a> </div> </td> 
 </tr>   
 
 <tr>
  <td> <b> <div align="center"> 14 </div> </b> </td>
  <td> <div align="center"> Inception_V3 <br> (ImageNet-1K weights) </div> </td>
  <td> <div align="center"> 27M </div> </td>
  <td> <div align="center"> --- </div> </td>
  <td> --- </td> 
  <td> <div align="center"> <a href="https://pytorch.org/vision/stable/models/generated/torchvision.models.inception_v3.html#torchvision.models.Inception_V3_Weights">Download</a> </div> </td> 
</tr>    

  
</table>
</div>

Current configuration of the ETAB weights for models reported on the leaderboard:

```python

weight_dict          = dict({"a0-A4-E": 0.2, "a0-A4-C": 0.2, "a0-A2-C": 0.2,
                             "a1-A4-C": 0.2, "a1-A2-C": 0.2})

```


## How to contribute?

Instructions on how to submit your model to the ETAB leaderboard will be posted soon!
