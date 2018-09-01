##
#
# Created by Rambod Rahmani.
# Section 4 - Image Theory
# text_on_images.py
#
##

import cv2
import numpy as np

# load the image
img = cv2.imread("me.jpg")

# normal size sans-serif font
font = cv2.FONT_HERSHEY_SIMPLEX

# the function putText renders the specified text string in the image. Symbols that
# cannot be rendered using the specified font are replaced by question marks.
cv2.putText(img, "Rambod Rahmani", (10, 390), font, 1, (255,255,255), 2)

# display the modified image
cv2.imshow("Rambod Rahmani Picture", img)

# wait for user input
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
