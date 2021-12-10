import numpy as np
from PIL import Image

# Load image as greyscale and make into Numpy array
grey = np.array(Image.open('4 segmentation.png').convert('L'))

# Load RGB LUT from CSV file
lut = np.loadtxt('autumn_cmap.csv', dtype=np.uint8, delimiter=',')

# Make output image, same height and width as grey image, but 3-channel RGB
result = np.zeros((*grey.shape,3), dtype=np.uint8)

# Take entries from RGB LUT according to greyscale values in image
np.take(lut, grey, axis=0, out=result)

# Save result
Image.fromarray(result).save('result_autumn.png')