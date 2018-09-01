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

# load the image
img = cv2.imread("me.jpg")

# load a copy of the original image taking the specified pixels
image = img[0:100, 0:100]

# display both images
cv2.imshow("Rambod Rahmani Picture", img)
cv2.imshow("Rambod Rahmani Picture Cut", image)

# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
