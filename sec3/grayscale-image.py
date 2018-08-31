##
 #
 # Created by Rambod Rahmani.
 # Section 3 - Color to Grayscale Conversion
 # grayscale-image.py
 #
 ##

import cv2
import numpy as np

# load image
img = cv2.imread("me.jpg")
cv2.imshow("Rambod Rahmani Picture (Original)", img)

# Conversion method 1
gr1 = cv2.imread("me.jpg", 0)
cv2.imshow("Rambod Rahmani Picture (Gr-1)", gr1)

# Conversion method 2
gr2 = cv2.imread("me.jpg")
grayImg = cv2.cvtColor(gr2, cv2.COLOR_BGR2GRAY)
cv2.imshow("Rambod Rahmani Picture (Gr-2)", grayImg)

# wait for user input
cv2.waitKey(0)

# destroy the windows
cv2.destroyAllWindows()
