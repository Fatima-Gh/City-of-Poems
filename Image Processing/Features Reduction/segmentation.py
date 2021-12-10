from skimage import data
import numpy as np
import matplotlib.pyplot as plt
# The I/O module is used for importing the image
from skimage import io
from skimage import util
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
import cv2
import dask.array as da
from combine_color import *
import argparse
import logging
import numpy as np
from time import time
# import utils as U
import codecs

logging.basicConfig(
                    #filename='out.log',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


###### CMD Arguements to load images #########

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image_name", dest="image_name", type=int, metavar='<int>', required=True, help="The path to the image.")
parser.add_argument("-vrs", "--verse_number", dest="verse", type=int, metavar='<int>', required=True, help="The line/verse number for the current image.")


args = parser.parse_args()

verse = args.verse
image_name = args.image_name


#Saving file as ‘image.png’
def save_images(image, name):
    name = name + '.png'
    io.imsave(name, image)

def image_show(image, nrows=1, ncols=1, cmap='BrBG_r'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='BrBG_r')
    ax.axis('off')
    return fig, ax

# Load images

path = "./Verse "+str(verse)+"/"
org_path = path + str(image_name) + ".png"
seg_path = path + str(image_name) + " segmentation.png"

image_gray = io.imread(seg_path)

# Recolor images

recolored_image = recolor(image_name, org_path, seg_path)
image = io.imread(recolored_image)
plt.imshow(image)
plt.show()


# SLIC(Simple Linear Iterative Clustering)

image_slic = seg.slic(image,n_segments=155)

# label2rgb replaces each discrete label with the average interior color
temp = color.label2rgb(image_slic, image, kind='avg')

plt.imshow(temp)
plt.show()

filename = 'SLIC_recolored_'+ str(verse)

save_images(temp, filename)

# Felzenszwalb
image_felzenszwalb = seg.felzenszwalb(image) 
plt.imshow(image_felzenszwalb)
plt.show()

np.unique(image_felzenszwalb).size

image_felzenszwalb_colored = color.label2rgb(image_felzenszwalb, image, kind='avg')
plt.imshow(image_felzenszwalb_colored)
plt.show()

filename = 'image_felzenszwalb_recolored_'+ str(verse)
save_images(image_felzenszwalb_colored, filename)

