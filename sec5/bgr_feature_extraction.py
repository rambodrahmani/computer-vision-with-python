##
#
# Created by Rambod Rahmani.
# Section 5 - Feature Extraction
# bgr_feature_extraction.py
#
# BGR Feature Extraction from color image.
#
##

import numpy as np
import cv2
import sys

# load the image
img = cv2.imread("me.jpg")

# display the loaded image
cv2.imshow("Feature Extraction", img)

# get loaded image data
height, width, depth = np.shape(img)

# Calculates an average (mean) of array elements.
# The function mean calculates the mean value M of array elements,
# independently for each channel, and return it.
means = cv2.mean(img)

# get blue color average
avgB = means[0]

# get green color average
avgG = means[1]

# get red color average
avgR = means[2]

# print extracted color averages
print( "Blue average: " + str(avgB) )
print( "Green average: " + str(avgG) )
print( "Red average: " + str(avgR) )

# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
