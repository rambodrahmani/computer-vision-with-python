##
 #
 # Created by Rambod Rahmani.
 # Section 3 - Metadata
 # metadata.py
 #
 ##

import cv2
import numpy as np

img = cv2.imread("me.jpg")
cv2.imshow("Rambod Rahmani Picture (Original)", img)

height,width,depth = np.shape(img)

print("height " + str(height))
print("width " + str(width))
print("depth " + str(depth))
print("")

# Conversion method 1
gr1 = cv2.imread("me.jpg", 0)
cv2.imshow("Rambod Rahmani Picture (Gr-1)", gr1)

print(gr1.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
