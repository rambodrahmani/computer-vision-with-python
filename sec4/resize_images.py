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

img = cv2.imread("me.jpg")
image = cv2.resize(img, (75,50))

cv2.imshow("Rambod Rahmani Picture", img)
cv2.imshow("Rambod Rahmani Picture Resized", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
