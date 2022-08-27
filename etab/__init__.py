import os
import subprocess

def install_seg_models():
    
    subprocess.call(["git", "clone", "https://github.com/sithu31296/semantic-segmentation"])
    os.chdir("semantic-segmentation")
    subprocess.call(["pip", 'install', "-e", "."])
    
if not os.path.isdir("semantic-segmentation"):
    
    install_seg_models()   