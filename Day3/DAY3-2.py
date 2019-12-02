# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:26:41 2019

@author: user
"""

import cv2

img_path = 'D:\\1st-DL-CVMarathon\\1st-DL-CVMarathon\\Day3\\lena.png'
img = cv2.imread(img_path,1)

cv2.imshow('img',img)


(B,G,R) = cv2.split(img)

#cv2.imshow('B',B)
#cv2.imshow('G',G)
#cv2.imshow('R',R)

img_B_equ = cv2.equalizeHist(B)
img_G_equ = cv2.equalizeHist(G)
img_R_equ = cv2.equalizeHist(R)
#cv2.imshow('eqB',img_B_equ)

img_mergeBGR = cv2.merge([img_B_equ,img_G_equ,img_R_equ])
cv2.imshow('img_mergeBGR',img_mergeBGR)

           
cv2.waitKey(0) #waitkey作用為不斷刷新圖像，0代表顯示第一偵圖
cv2.destroyAllWindows() #按下任意鍵關閉所有視窗)