import numpy as np
from matplotlib import cm

# Get 256 entries from "viridis" or any other Matplotlib colormap
colmap = cm.get_cmap('viridis', 256)

# Make a Numpy array of the 256 RGB values
# Each line corresponds to an RGB colour for a greyscale level
np.savetxt('cmap.csv', (colmap.colors[...,0:3]*255).astype(np.uint8), fmt='%d', delimiter=',')


# Get "autumn" colourmap
colmap = cm.get_cmap('autumn')

# Save 256 RGB entries as CSV - one for each of grey levels 0..255
np.savetxt('autumn_cmap.csv', np.array([colmap(i/255)[:3] for i in range(256)]) * 255, fmt="%d", delimiter=',')