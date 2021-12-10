import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import cv2

def save_images(image, name):
    #Saving file as ‘image.png’
    name = name + '.png'
    io.imsave(name, image)

def recolor(image_name, org_name, seg_name):
    rgb = cv2.imread(org_name)
    rgb = rgb.astype('uint8')

    resized_image = cv2.resize(rgb, (256, 256), interpolation=cv2.INTER_AREA)

    rgb = resized_image

    gray = io.imread(seg_name)

    gray = gray.astype('uint8')


    # Create random color image
    image = np.zeros((256, 256, 3), dtype="uint8") # (np.random.standard_normal([256, 256, 3]) * 255).astype(np.uint8)

    # Merge channels to create color image(3 channels)
    gray_three = cv2.merge([gray, gray, gray])
    # resized_image = cv2.resize(gray_three, (512, 512))

    gray_three = gray_three.astype('uint8')
    print('rgb shape ====> ', rgb.shape, rgb.dtype)
    print('gray shape ====> ', gray.shape, gray.dtype)
    print('image shape ====> ', image.shape, image.dtype)
    print('gray_three shape ====> ', gray_three.shape, gray_three.dtype)

    final_result = cv2.bitwise_or(rgb, gray_three, image)
    plt.imshow(final_result)
    plt.show()

    name = 'recolored_' + str(image_name)
    print("Recolored name ---> ", name)
    save_images(final_result, name)
    name = name + ".png"
    return name
