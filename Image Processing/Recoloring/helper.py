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
import utils as U
import codecs

def load_images():
    images = io.ImageCollection('../images/*.png:../images/*.jpg')
    print('Type:', type(images))
    """
    images.files
    Out[]: Type: <class ‘skimage.io.collection.ImageCollection’>
    """