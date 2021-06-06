import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('Front.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)

fig = plt.figure()
ax = plt.axes(projection = '3d')
cv2.imshow('Corner',img)
print(corners)
plt.imshow(img)
plt.show()
