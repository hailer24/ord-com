gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray =np.float32(gray)
coords = 255*(gray < 128).astype(np.uint8) 
coords = cv2.findNonZero(coords) 
x, y, w, h = cv2.boundingRect(coords) 
img = img[y-10:y+h+10, x-10:x+w+10]
gray = gray[y-10:y+h+10, x-10:x+w+10]
cv2.imshow("Cropped", img)
corn = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corn = np.int0(corn)
for corner in corn:
    x,y = corner.ravel()
    #print(x,y)
    cv2.circle(img,(x,y),3,255,-1)
##print(type(corn))
##print(corn)
zs = [1 for x in corn]
xs = [int(x[0][0]/50)*5 for x in corn]
ys = [int((x[0][1])/50)*(-5) for x in corn]
fig, (ax1, ax2) = plt.subplots(1, 2)
#print(len(xs))
for i in range(len(xs)):
    x = [xs[i],xs[i]]
    y = [ys[i],ys[i]]
    z = [-40,40]
    #print(xs[i]+','+ys[i])
    ax.plot(x,y,z,c='green')
ax1.scatter(xs,ys)
ax2.imshow(img)
return corn
