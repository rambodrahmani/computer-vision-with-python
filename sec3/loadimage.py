##
 #
 # Created by Rambod Rahmani.
 # Section 3 - Load Image
 # loadimage.py
 #
 ##

import cv2
import numpy as np

img = cv2.imread("me.jpg")
cv2.imshow("Rambod Rahmani Picture", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
