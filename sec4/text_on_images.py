##
 #
 # Created by Rambod Rahmani.
 # Section 4 - Image Theory
 # text_on_images.py
 #
 ##

import cv2
import numpy as np

img = cv2.imread("me.jpg")

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Rambod Rahmani", (10, 390), font, 1, (255,255,255), 2)

cv2.imshow("Rambod Rahmani Picture", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
