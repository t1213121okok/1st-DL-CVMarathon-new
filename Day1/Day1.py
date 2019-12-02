# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:27:45 2019

@author: user
"""

import cv2
import os


relative_path = os.path.relpath(r'D:\1st-DL-CVMarathon\1st-DL-CVMarathon\Day1\lena.png')
#img = cv2.imread(relative_path , cv2.IMREAD_COLOR)



#imread 讀取圖片
img = cv2.imread(relative_path , cv2.IMREAD_COLOR) #cv2.IMREAD_COLOR can alos replace with 1
img2 = cv2.imread(relative_path , cv2.IMREAD_GRAYSCALE) #cv2.IMREAD_GRAYSCALE can also replace with 0

#cv2.IMREAD_UNCHANGED : 包含透明通道 (-1)






cv2.imshow('rgb', img)
cv2.imshow('rbg2',img2)
cv2.waitKey(0) #waitkey作用為不斷刷新圖像，0代表顯示第一偵圖
cv2.destroyAllWindows() #按下任意鍵關閉所有視窗



