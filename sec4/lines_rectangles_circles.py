##
#
# Created by Rambod Rahmani.
# Section 4 - Image Theory
# lines_rectangles_circles.py
#
##

import cv2
import numpy as np

# load the image
img = cv2.imread("me.jpg")

# draw a line on the given image, from pixel (0, 0) to (100, 100) with
# the given color and thickness
cv2.line(img, (0,0), (100,100), (0,0,255), 5)

# draw a rectangle
cv2.rectangle(img, (0,300), (100,200), (0,0,255), 10)

# draw a circle
cv2.circle(img, (200,200), 64, (0,0,230), 3)

# display the modified image
cv2.imshow("Rambod Rahmani Picture", img)

# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
