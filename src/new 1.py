import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import matplotlib.image as mpimg

img = cv2.imread('Bottom.png') # Read in the image and convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = 255*(gray < 128).astype(np.uint8) # To invert the text to white
cv2.imshow("g",gray)
coords = cv2.findNonZero(gray) # Find all non-zero points (text)
x, y, w, h = cv2.boundingRect(coords) # Find minimum spanning bounding box
if w>h:
    h = w
else :
    w = h
rect = gray[y-10:y+h+10, x-10:x+w+10] # Crop the image - note we do this on the original image
cv2.waitKey(0)
cv2.destroyAllWindows()
imgplt = plt.imshow(gray)
plt.show()


