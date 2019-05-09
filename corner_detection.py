import numpy as np
import cv2
from matplotlib import pyplot as plt

size_h=4
size_s=4
img = cv2.imread('121.png')
img = cv2.GaussianBlur(img,(9,9),0)
ret, binary = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
gray = cv2.cvtColor(binary, cv2.COLOR_BGR2GRAY)
l = list()
pattern_size=(size_h,size_s)
found, corners=cv2.findChessboardCorners(gray,pattern_size )
cv2.drawChessboardCorners(img, pattern_size, corners, found)

print(corners)
for c in corners:
    #print(len(corners))
    x,y = c.ravel()
    l.append((x,y))

plt.imshow(img),plt.show()
