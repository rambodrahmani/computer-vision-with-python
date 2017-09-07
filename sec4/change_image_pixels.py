##
 #
 # Created by Rambod Rahmani.
 # Section 4 - Image Theory
 # change_image_pixels.py
 #
 ##

import cv2
import numpy as np

img = cv2.imread("me.jpg")
cv2.imshow("Rambod Rahmani Picture", img)

height, width, depth = np.shape(img)

for i in range(0, width):
	img[1][i][0] = 255
	img[1][i][1] = 255
	img[1][i][2] = 255
cv2.imshow("Rambod Rahmani Picture 2", img)

img = cv2.imread("me.jpg")
for j in range(0, height):
	for i in range(0, width):
		img[j][i][0] = 255
		img[j][i][1] = 255
		img[j][i][2] = 255
cv2.imshow("Rambod Rahmani Picture 3", img)

img = cv2.imread("me.jpg")
for j in range(0, height):
	for i in range(0, width):
		img[j][i][0] = 0
		img[j][i][1] = 0
		img[j][i][2] = 0
cv2.imshow("Rambod Rahmani Picture 4", img)

img = cv2.imread("me.jpg")
for j in range(0, height):
	for i in range(0, width):
		img[j][i][0] = 0
cv2.imshow("Rambod Rahmani Picture 5", img)

img = cv2.imread("me.jpg")
for j in range(0, height):
	for i in range(0, width):
		img[j][i][1] = 0
cv2.imshow("Rambod Rahmani Picture 6", img)

img = cv2.imread("me.jpg")
for j in range(0, height):
	for i in range(0, width):
		img[j][i][2] = 0
cv2.imshow("Rambod Rahmani Picture 7", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
