# -*- coding: UTF-8 -*-
import  os
import cv2
import corner_detection
import numpy as np
import matplotlib.pyplot as plt
img = corner_detection.img
l=jdv3.l
size_h=jdv3.size_h
size_s=jdv3.size_s

rows, cols = img.shape[:2] # row 竖，cols 横
shu=rows/(size_s-1) #小方块的竖
heng= cols/(size_h-1) #小方块的横
# pts1 = np.float32([l[3], l[4], l[6], l[7]])
# pts2 = np.float32([[0, 0], [heng, 0], [0, shu], [heng, shu]])
# M = cv2.getPerspectiveTransform(pts1, pts2)
# dst = cv2.warpPerspective(img, M, (int(heng), int(shu)))
path='G:\\tp\\'
for i in range(size_s-1):
    for j in range(size_h-1):
        # i=1
        # j=0
        #print(i*size_h+j,i*size_h+j+1,size_h*(i+1)+j,size_h+(i+1)+j+1)
        pts1 = np.float32([l[i*size_h+j], l[i*size_h+j+1], l[size_h*(i+1)+j], l[size_h*(i+1)+j+1]])
        pts2 = np.float32([[0, 0], [heng, 0], [0, shu], [heng, shu]])
        M =cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(img, M, (int(heng), int(shu)))
        fname=i*(size_s-1)+j
        #print(fname)
        cv2.imwrite(path+'%d.jpg'%fname,dst)

plt.subplot(121), plt.imshow(img[:, :, ::-1]), plt.title('input')
#plt.subplot(122), plt.imshow(dst[:, :, ::-1]), plt.title('output')
# img[:, :, ::-1]是将BGR转化为RGB
plt.show()
