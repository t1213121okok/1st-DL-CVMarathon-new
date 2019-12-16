# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:05:22 2019

@author: user
"""

import cv2
import numpy as np



img_path = 'D:\\1st-DL-CVMarathon\\1st-DL-CVMarathon\\Day6\\lena.png'
img = cv2.imread(img_path,1)

row, col = img.shape[:2]

#旋轉矩陣
M_rotate = cv2.getRotationMatrix2D((col//2,row//2),45,0.5)
#平移矩陣
M_trans = np.array([[1,0,100],[0,1,-50]],dtype=np.float32)

#選轉

img_rot = cv2.warpAffine(img,M_rotate,(col,row))

#平移
img_rot_trans = cv2.warpAffine(img_rot,M_trans,(col,row))

img_show = np.hstack((img,img_rot,img_rot_trans))
img_show_resize = cv2.resize(img_show,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)


while True:
    cv2.imshow('Rotate 45 , scale 0.5, x=100,y=-50', img_show_resize)
    k=cv2.waitKey(0)
    if k ==27:
        cv2.destroyAllWindows()
        break




