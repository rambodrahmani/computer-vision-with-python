##
#
# Created by Rambod Rahmani.
# Section 5 - Feature Extraction
# colorFeature.py
#
# BGR Feature Extraction from color image.
#
##

import numpy as np
import cv2
import sys

##
# Extracts BGR feature from the given image.
##
def colorFeature(img):
	means = cv2.mean(img)

	avgB = int(means[0])
	avgG = int(means[1])
	avgR = int(means[2])

	return [avgB,avgG, avgR]

##
# Devides the given image into the given number of blocks.
##
def divideImage(img, blocks):
	windowsize_r = img.shape[0] / blocks
	windowsize_c = img.shape[1] / blocks

	windowsize_r = int(windowsize_r)
	windowsize_c = int(windowsize_c)

	images = []
	for r in range(0, img.shape[0], windowsize_r):
		for c in range(0, img.shape[0], int(windowsize_c)):
			window = img[r:r+windowsize_r, c:c+windowsize_c]
			images.append(window)

	return images


##
# Devides the given image in the givne number of blocks and decribes each
# block using color feature extraction.
##
def describeImage(img, blocks):
	featureVector = []
	images = divideImage(img,blocks)
	
	for image in images:
		means = colorFeature(image)

		featureVector.append( means[0] )
		featureVector.append( means[1] )
		featureVector.append( means[2] )

	return featureVector

##
# Calculates the distance between x and y.
##
def distance(x,y):
	sumSq=0.0
	for i in range(len(x)):
		sumSq+=(x[i]-y[i])**2
	return (sumSq**0.5)


# load the image
img = cv2.imread("car.jpeg")

# display the loaded image
cv2.imshow("colorFeature Extraction", img)

# retrieve image feature vector
featureVector = describeImage(img,2)

# print image feature vector
print(featureVector)

# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
