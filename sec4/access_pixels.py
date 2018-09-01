##
#
# Created by Rambod Rahmani.
# Section 4 - Image Theory
# access_pixels.py
#
# You can access a pixel value by its row and column coordinates. For BGR image,
# it returns an array of Blue, Green, Red values. For grayscale image, just
# corresponding intensity is returned.
#
# Warning: Numpy is a optimized library for fast array calculations. So simply
# accessing each and every pixel values and modifying it will be very slow and it
# is discouraged.
#
##

import cv2
import numpy as np

# load image
img = cv2.imread("me.jpg")

# print RGB values for the pixel 1,1
print(img[1][1])

# set R (0), G (1) and B (2) values for the pixel 1,1
img[1][1][0] = 255
img[1][1][1] = 255
img[1][1][2] = 255

# pixel coordinates
py = 100
px = 100

# set RGB values
img[px][py][0] = 255
img[px][py][1] = 255
img[px][py][2] = 255

# show image in the window
cv2.imshow("Rambod Rahmani Picture", img)

# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
