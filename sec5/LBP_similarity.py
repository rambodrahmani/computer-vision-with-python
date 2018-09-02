##
#
# Created by Rambod Rahmani.
# Section 5 - Feature Extraction
# LBP_similarity.py
#
# Local binary patterns:
# ----------------------
# Local binary patterns (LBP) is a type of visual descriptor used for classification 
# in computer vision. LBP is the particular case of the Texture Spectrum model proposed 
# in 1990. LBP was first described in 1994. It has since been found to be a 
# powerful feature for texture classification; it has further been determined that when 
# LBP is combined with the Histogram of oriented gradients (HOG) descriptor, it 
# improves the detection performance considerably on some datasets. A comparison of 
# several improvements of the original LBP in the field of background subtraction was 
# made in 2015 by Silva et al. A full survey of the different versions of LBP can be 
# found in Bouwmans et al.
#
# How it works:
# -------------
# The LBP feature vector, in its simplest form, is created in the following manner:
#	1. Divide the examined window into cells (e.g. 16x16 pixels for each cell).
#	2. For each pixel in a cell, compare the pixel to each of its 8 neighbors (on 
#	   its left-top, left-middle, left-bottom, right-top, etc.). Follow the pixels 
#	   along a circle, i.e. clockwise or counter-clockwise.
#	3. Where the center pixel's value is greater than the neighbor's value, write 
#	   "0". Otherwise, write "1". This gives an 8-digit binary number (which is usually 
#	   converted to decimal for convenience).
#	4. Compute the histogram, over the cell, of the frequency of each "number" occurring
#	   (i.e., each combination of which pixels are smaller and which are greater than
#	   the center). This histogram can be seen as a 256-dimensional feature vector.
#	5. Optionally normalize the histogram.
#	6. Concatenate (normalized) histograms of all cells. This gives a feature vector
#	   for the entire window.
#
# The feature vector can now be processed using the Support vector machine, extreme 
# learning machines, or some other machine-learning algorithm to classify images. Such 
# classifiers can be used for face recognition or texture analysis.
##

import numpy as np
import cv2
import sys

# load the image
img = cv2.imread("car.jpeg")

# display the loaded image
cv2.imshow("Gray scale image Histogram", img)



# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
