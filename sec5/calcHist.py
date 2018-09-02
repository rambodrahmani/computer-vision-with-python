##
#
# Created by Rambod Rahmani.
# Section 5 - Feature Extraction
# calcHist.py
#
# Calculate histograms of arrays of images by using the OpenCV function calcHist.
# Normalize an array by using the function normalize.
#
# Image histogram:
# ----------------
# An image histogram is a type of histogram that acts as a graphical representation
# of the tonal distribution in a digital image. It plots the number of pixels for
# each tonal value. By looking at the histogram for a specific image a viewer will
# be able to judge the entire tonal distribution at a glance.
#
##

import numpy as np
import cv2
import sys

# load the image
img = cv2.imread("car.jpeg")

# display the loaded image
cv2.imshow("Gray scale image Histogram", img)

# retrieve image histogram
hist = cv2.calcHist([img], [0], None, [10], [0, 256])

# normalize image histogram values
cv2.normalize(hist, hist).flatten()

# print image histogram values
print(hist)

# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
