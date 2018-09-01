##
#
# Created by Rambod Rahmani.
# Section 4 - Image Theory
# change_image_pixels.py
#
##

import cv2
import numpy as np

# load and display image me.jpg
img = cv2.imread("me.jpg")
cv2.imshow("Rambod Rahmani Picture", img)

# get image shape data
height, width, depth = np.shape(img)

# change all image pixels in the first row
for i in range(0, width):
	img[1][i][0] = 255
	img[1][i][1] = 255
	img[1][i][2] = 255

# show the modified image
cv2.imshow("Rambod Rahmani Picture 2", img)

# reload the image, edit all pixels: white color
img = cv2.imread("me.jpg")
for j in range(0, height):
	for i in range(0, width):
		img[j][i][0] = 255
		img[j][i][1] = 255
		img[j][i][2] = 255
cv2.imshow("Rambod Rahmani Picture 3", img)

# reload the image, edit all pixels: black color color
img = cv2.imread("me.jpg")
for j in range(0, height):
	for i in range(0, width):
		img[j][i][0] = 0
		img[j][i][1] = 0
		img[j][i][2] = 0
cv2.imshow("Rambod Rahmani Picture 4", img)

# reload the image, edit R channel
img = cv2.imread("me.jpg")
for j in range(0, height):
	for i in range(0, width):
		img[j][i][0] = 0
cv2.imshow("Rambod Rahmani Picture 5", img)

# reload the image, edit G channel
img = cv2.imread("me.jpg")
for j in range(0, height):
	for i in range(0, width):
		img[j][i][1] = 0
cv2.imshow("Rambod Rahmani Picture 6", img)

# reload the image, edit B channel
img = cv2.imread("me.jpg")
for j in range(0, height):
	for i in range(0, width):
		img[j][i][2] = 0
cv2.imshow("Rambod Rahmani Picture 7", img)

# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
