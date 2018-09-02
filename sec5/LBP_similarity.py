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

import os
import cv2
import glob
import numpy as np
from scipy.stats import itemfreq
from skimage.feature import local_binary_pattern


try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

import tkinter
import tkinter.constants
import tkinter.filedialog

##
# Loads the image at the given filename path. Resizes the loaded image.
# Calculates the local binary pattern of the loaded image using uniform method.
# Calculates and returns a feature vector for the loaded image based on the calculated LBP.
##
def imageToFeature(filename):
	img = cv2.imread(filename, 0)
	img = cv2.resize(img, (200, 100))
	lbp = local_binary_pattern(img, 8*3, 3, method='uniform')
	x = itemfreq(lbp.ravel())
	feature = x[:, 1]/sum(x[:, 1])

	return feature

##
# Calculates the distance (difference) between x and y.
##
def distance(x, y):
	sumSq=0.0

	for i in range(len(x)):
		sumSq+=(x[i]-y[i])**2

	return (sumSq**0.5)

# similarity threshold
closestDistance = 99999999

# path of the most similar image found
mostSimilarImage = ""

print("This program will search for the given filename in the ./images folder using Local binary patterns.")

# ask user to input search filename
query = input("Enter filename: ")

# get feature vector for the provided image
queryFeature = imageToFeature(query)

# loop through the pictures in the images folder
for filename in glob.iglob('images/*.*'):
	# for each image in the images folder
	# calculate the feature vector using LBP
	databaseFeature = imageToFeature(filename)

	# calculate the difference between the feature vector of the loaded image and the
	# current directory image
	dist = distance(queryFeature,databaseFeature)

	# if the difference is lower than the acceptable threshold
	if dist < closestDistance:
		# one of the the most similar image to the given one has been found
		closestDistance = dist
		mostSimilarImage = filename

# show result
print(mostSimilarImage)

# load the image provided by the user
queryImg = cv2.imread(query, 1)

# loaded the most image that has been found
mostSimilarImg = cv2.imread(mostSimilarImage, 1)

# display both images
cv2.imshow("Query ", queryImg)
cv2.imshow("Most Similar ", mostSimilarImg)

# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
