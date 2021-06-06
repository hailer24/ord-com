import numpy as np
import cv2
import matplotlib.pyplot as plt
ax = plt.axes(projection ='3d')
fig, (ax1, ax2) = plt.subplots(1, 2)
def coords(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray =np.float32(gray)
    coords = 255*(gray < 128).astype(np.uint8) 
    coords = cv2.findNonZero(coords) 
    x, y, w, h = cv2.boundingRect(coords) 
    img = img[y-10:y+h+10, x-10:x+w+10]
    gray = gray[y-10:y+h+10, x-10:x+w+10]
    corn = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    corn = np.int0(corn)
    for corner in corn:
        x,y = corner.ravel()
        cv2.circle(img,(x,y),3,255,-1)
    zs = [1 for x in corn]
    xs = [int(x[0][0]/50)*5 for x in corn]
    ys = [int((x[0][1])/50)*(5) for x in corn]
    return [xs,ys]

print('Enter Top Name:')
PATH = input()
img = cv2.imread(PATH)
Top=coords(img)
#cv2.imshow('a',img)
for i in range(len(Top[1])):
    Top[0][i] *= -1
sub = min(Top[0])
for i in range(len(Top[1])):
    Top[0][i] -= sub
ax1.scatter(Top[0],Top[1])

print(Top)
print('Enter Bottom Name:')
PATH = input()
img = cv2.imread(PATH)
Bottom = coords(img)
#ax.scatter(Bottom[0],Bottom[1])
ax1.scatter(Bottom[0],Bottom[1])
#cv2.imshow('b',img)
print(Bottom)
plt.show()
