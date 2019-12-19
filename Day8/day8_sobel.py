# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 21:31:20 2019

@author: user
"""

#Gaussian Blur
# img_blur = cv2.GaussianBlur(img,(3,3),0)

#Sobel
# img_x = cv2.Sobel(img_gray,cv2.CV_16S,dx=1,dy=0,ksize=3)
# img_y = ...

# img_x = cv2.convertScaleAbs(img_x)
# img_y = cv2.convertScaleAbs(img_y)
# img_sobel = cv2.addWeight(img_x,0.5,img_y,0.5,0)

import cv2
import numpy as np

img_path = 'D:\\1st-DL-CVMarathon\\1st-DL-CVMarathon\\Day8\\lena.png'
img = cv2.imread(img_path,1)

#模糊

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_sobel_x = cv2.Sobel(img_gray,cv2.CV_16S,dx=1,dy=0,ksize=3)
img_sobel_x_uint8 = cv2.Sobel(img_gray,cv2.CV_8U,dx=1,dy=0,ksize=3)

img_sobel_x_tran = cv2.convertScaleAbs(img_sobel_x)




img_out = np.hstack((img_sobel_x_tran,img_sobel_x_uint8))

#while True:
#    cv2.imshow('comparable',img_out)
#    k=cv2.waitKey(0)
#    if k ==27:
#        cv2.destroyAllWindows()
#        break
    
    
img_sobel_x1 = cv2.Sobel(img_gray,cv2.CV_16S,1,0,ksize=3)
img_sobel_x2 = cv2.Sobel(img_gray,cv2.CV_16S,2,0,ksize=3)

img_sobel_x1_u8 = cv2.convertScaleAbs(img_sobel_x1)
img_sobel_x2_u8 = cv2.convertScaleAbs(img_sobel_x2)


img_sobel_times = np.hstack((img_sobel_x1_u8,img_sobel_x2_u8))

while True:
    cv2.imshow('comparable',img_out)
    cv2.imshow('img_sobel_times',img_sobel_times)
    k=cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break




