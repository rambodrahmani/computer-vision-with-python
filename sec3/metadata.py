##
#
# Created by Rambod Rahmani.
# Section 3 - Metadata
# metadata.py
#
# Image properties include number of rows, columns and channels, type of image
# data, number of pixels etc. Shape of image is accessed by img.shape. It
# returns a tuple of number of rows, columns and channels (if image is color).
#
# Note: If image is grayscale, tuple returned contains only number of rows and
# columns. So it is a good method to check if loaded image is grayscale or color
# image.
#
##

import cv2
import numpy as np

# load image
img = cv2.imread("me.jpg")
cv2.imshow("Rambod Rahmani Picture (Original)", img)

# extract loaded image info
height,width,depth = np.shape(img)

# print extracted info to the terminal
print("height " + str(height))
print("width " + str(width))
print("depth " + str(depth))
print("")

# reload the image in grayscale
gr1 = cv2.imread("me.jpg", 0)
cv2.imshow("Rambod Rahmani Picture (Gr-1)", gr1)

# print gray scale image info to the terminal
print(gr1.shape)

# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
