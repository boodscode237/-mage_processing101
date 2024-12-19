# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 00:56:06 2024

@author: abodo
"""
# pillow
# pip install pillow
from PIL import Image
import numpy as np
 
img = Image.open("images/monkey.jpg")
print(type(img))
#img.show()
print(img.format)

img1 = np.asarray(img)

print(type(img1))

##############################################
# In Matplotlib
# pip install matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread("images/monkey.jpg") 
print(type(img))
print(img.shape)
plt.imshow(img)
plt.colorbar()
####################################

#scikit-image
from skimage import io, img_as_float
import numpy as np
image = io.imread('images/monkey.jpg').astype(np.float32)

print(type(image))
print(image.shape)
plt.imshow(image)
plt.colorbar()

image_float = img_as_float(image)
print(image_float)

############
import cv2
import matplotlib.pyplot as plt

grey_image = cv2.imread('images/monkey.jpg', 0)
color_image = cv2.imread('images/monkey.jpg', 1)

cv2.imshow("Grey Image", grey_image)
cv2.imshow("Color image", color_image)
plt.imshow(color_image, cv2.COLOR_BGR2HSV)
cv2.waitKey(0)
cv2.destroyAllWindows()
#############
import czifile

img = czifile.imread('images/test_image.czi')
print(img.shape)
###############
from apeer_ometiff_library import io

(pic2, omexml) = io.read_ometiff("images/test_image.ome.tif")
print(pic2.shape)
###########