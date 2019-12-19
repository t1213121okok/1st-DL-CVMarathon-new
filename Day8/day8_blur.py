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

img_blur_copy = img.copy()


img_blur_5X5_1 = cv2.GaussianBlur(img_blur_copy,(5,5),0)
img_blur_5X5_2 = cv2.GaussianBlur(img_blur_5X5_1,(5,5),0)
img_blur_5X5_3 = cv2.GaussianBlur(img_blur_5X5_2,(5,5),0)
img_blur_5X5 = np.hstack((img_blur_5X5_1,img_blur_5X5_2,img_blur_5X5_3))



img_blur_3X3_1 = cv2.GaussianBlur(img_blur_copy,(3,3),0)
img_blur_3X3_2 = cv2.GaussianBlur(img_blur_3X3_1,(3,3),0)
img_blur_3X3_3 = cv2.GaussianBlur(img_blur_3X3_2,(3,3),0)
img_blur_3X3 = np.hstack((img_blur_3X3_1,img_blur_3X3_2,img_blur_3X3_3))

img_blur_result = np.vstack((img_blur_5X5,img_blur_3X3))

img_blur_result =   cv2.resize(img_blur_result,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)


while True:
    cv2.imshow('img_blur_result',img_blur_result)
    k=cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break










