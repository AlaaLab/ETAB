from PIL import Image
import torchvision.transforms as T
from pathlib import Path
import config
import numpy as np
import torch

PIL_transform   = T.ToPILImage()

def create_echo_clip(one_patient_echo, op_file_name):

    if not type(one_patient_echo)==list:
      
      one_patient_echo = [torch.einsum("chw->hwc", one_patient_echo[k, :, :, :]) for k in range(one_patient_echo.shape[0])] 
  
    Path(config.clip_dir).mkdir(parents=True, exist_ok=True)
    echo_frames = []
    out_dir     = config.clip_dir + op_file_name + ".gif"

    for u in range(len(one_patient_echo)):
        
        echo_image  = one_patient_echo[u]

        echo_frames.append(PIL_transform((echo_image * 255).detach().numpy().astype(np.uint8)))

    echo_frames[0].save(out_dir, 
                        save_all=True, 
                        append_images=echo_frames[1:], optimize=False, duration=50, loop=0)  
  