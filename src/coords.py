import numpy as np
import cv2
import matplotlib.pyplot as plt
ax = plt.axes()
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
    xs = [int(x[0][0]) for x in corn]
    subx = min(xs)
    ys = [int((x[0][1])) for x in corn]
    suby = min(ys)
    for i in range(len(xs)):
        xs[i] -=subx
        ys[i] -=suby
        xs[i] = (int((xs[i]+5)/50)*5+int((xs[i])/50)*5)/2
        ys[i] = (int((ys[i]+5)/50)*5+int((ys[i]+5)/50)*5)/2
    return [xs,ys]

print('Enter Top Name:')
#PATH = input()
img = cv2.imread('Top.png')
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
#PATH = input()
img = cv2.imread('Bottom.png')
Bottom = coords(img)
#ax.scatter(Bottom[0],Bottom[1])
ax1.scatter(Bottom[0],Bottom[1])
#cv2.imshow('b',img)
print(Bottom)
#############################################################3
print('Enter Left Name:')
#PATH = input()
img = cv2.imread('Left.png')
Left=coords(img)
#cv2.imshow('a',img)
for i in range(len(Left[1])):
    Left[0][i] *= -1
sub = min(Left[0])
for i in range(len(Left[1])):
    Left[0][i] -= sub
ax2.scatter(Left[0],Left[1],5)
print(Left)
print('Enter Right Name:')
#PATH = input()
img = cv2.imread('Right.png')
Right = coords(img)
#ax.scatter(Bottom[0],Bottom[1])
ax2.scatter(Right[0],Right[1])
#cv2.imshow('b',img)
print(Right)
###########################################################
print('Enter Front Name:')
#PATH = input()
img = cv2.imread('Front.png')
Front=coords(img)
#cv2.imshow('a',img)
for i in range(len(Front[1])):
    Front[0][i] *= -1
sub = min(Front[0])
for i in range(len(Front[1])):
    Front[0][i] -= sub
ax.scatter(Front[0],Front[1],10)

print(Front)
print('Enter Back Name:')
#PATH = input()
img = cv2.imread('Back.png')
Back = coords(img)
#ax.scatter(Back[0],Back[1])
ax.scatter(Back[0],Back[1],10)
#cv2.imshow('b',img)
print(Back)
plt.show()
