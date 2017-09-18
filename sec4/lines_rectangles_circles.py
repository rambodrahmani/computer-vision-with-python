##
 #
 # Created by Rambod Rahmani.
 # Section 4 - Image Theory
 # lines_rectangles_circles.py
 #
 ##

import cv2
import numpy as np

img = cv2.imread("me.jpg")

cv2.line(img, (0,0), (100,100), (0,0,255), 5)

cv2.rectangle(img, (0,300), (100,200), (0,0,255), 10)

cv2.circle(img, (200,200), 64, (0,0,230), 3)

cv2.imshow("Rambod Rahmani Picture", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
