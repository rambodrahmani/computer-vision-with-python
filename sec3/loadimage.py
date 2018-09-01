##
#
# Created by Rambod Rahmani.
# Section 3 - Load Image
# loadimage.py
#
##

import cv2
import numpy as np

# load image
img = cv2.imread("me.jpg")
cv2.imshow("Rambod Rahmani Picture", img)

# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
