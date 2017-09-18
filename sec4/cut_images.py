##
 #
 # Created by Rambod Rahmani.
 # Section 4 - Image Theory
 # cut_images.py
 #
 ##

import numpy as np
import cv2
import sys

img = cv2.imread("me.jpg")
image = img[0:100,0:100]

cv2.imshow("Rambod Rahmani Picture", img)
cv2.imshow("Rambod Rahmani Picture Cut", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
