##
#
# Created by Rambod Rahmani.
# Section 4 - Image Theory
# resize_images.py
#
##

import numpy as np
import cv2
import sys

# load the image
img = cv2.imread("me.jpg")

# create a copy image with different width and height
image = cv2.resize(img, (75,50))

# display both images
cv2.imshow("Rambod Rahmani Picture", img)
cv2.imshow("Rambod Rahmani Picture Resized", image)

# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
