from skimage import measure
from matplotlib import pyplot as plt
import torch


def plot_segment(image, segment, overlay=True, color="r"):
    
    image      = torch.einsum("chw->hwc", image).detach().numpy()
    segment    = segment.detach().numpy()
    
    contours   = measure.find_contours(segment, 0.8)

    # Select the largest contiguous contour
    contour    = sorted(contours, key=lambda x: len(x))[-1]

    # Display the image and plot the contour
    
    fig, ax  = plt.subplots()
    
    if overlay:

        ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray)

        X, Y     = ax.get_xlim(), ax.get_ylim()

        ax.step(contour.T[1], 
                contour.T[0], 
                linewidth=5, 
                c=color)
    
    
    
        ax.imshow(segment, interpolation='nearest', alpha=0.5, cmap=plt.cm.gray)
    
    else:
        
        ax.imshow(segment, interpolation='nearest', cmap=plt.cm.gray)
        
        X, Y     = ax.get_xlim(), ax.get_ylim()

        ax.step(contour.T[1], 
                contour.T[0], 
                linewidth=5, 
                c=color)
    
    

    ax.set_xlim(X), ax.set_ylim(Y)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()