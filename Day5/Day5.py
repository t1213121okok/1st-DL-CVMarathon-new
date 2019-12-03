# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:52:23 2019

@author: user
"""

#note
#使用CV2畫圖

'''
cv2.rectangle(
    image,                   #圖片
    (60,40),                 #左上角座標
    (420,510),               #右下角座標
    (0,0,255),               #BGR顏色
    3)                       #線的寬度 ; 負值表示將圖填滿

cv2.line(
    image,                   #圖片
    (60,40),                 #左上角座標
    (420,510),               #右下角座標
    (0,0,255),               #BGR顏色
    3)                       #線的寬度 ; 負值表示將圖填滿


cv2.putText(
    image,
    '(60,40)',        #要加的字
    (60,40),          #文字左下角位置
    0,                #字型
    3,                #字體大小
    (0,0,255),
    2)

'''



import cv2
import numpy as np

img_path = 'D:\\1st-DL-CVMarathon\\1st-DL-CVMarathon\\Day5\lena.png'
img = cv2.imread(img_path,1)
img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_HSV[...,2] = cv2.equalizeHist(img_HSV[...,2])
img_HSV_eq = cv2.cvtColor(img_HSV,cv2.COLOR_HSV2BGR)

#先畫紅框
cv2.rectangle(img_HSV_eq,(60,40),(420,510),(0,0,255),3)


#轉向 & 0.5倍
img_HSV_eq_H_mirror = img_HSV_eq[:,::-1,:]
img_HSV_eq_H_mirror_0_5x = cv2.resize(img_HSV_eq_H_mirror,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)

while True:
    cv2.imshow('result',img_HSV_eq_H_mirror_0_5x)
    
    k = cv2.waitKey(0)
    if k ==27:
        cv2.destroyAllWindows()
        break


##method2

point1 = [60,40]
point2 = [420,510]

#after mirror 
point1[0] = -60
point2[0] = -420

#shrink ratio
x_fac = 0.5
y_fac = 0.5     

#resize col / row
#resize_column = int(img_HSV_eq.shape[1]*x_fac)
#resize_row = int(img_HSV_eq.shape[0]*y_fac)

M = np.array([[0.5,0,0],[0,0.5,0]],dtype=np.float32)
box = np.array([point1,point2],dtype=np.float32)

resize_position = np.dot(M.T,box)
resize_position = resize_position.astype('uint8')

resize_p1 = tuple(resize_position[0])
resize_p2 = tuple(resize_position[1])


print(resize_p1,resize_p2)


cv2.rectangle(img_HSV_eq_H_mirror_0_5x,resize_p1,resize_p2,(255,0,0),3)



while True:
    cv2.imshow('result',img_HSV_eq_H_mirror_0_5x)
    
    k = cv2.waitKey(0)
    if k ==27:
        cv2.destroyAllWindows()
        break



 

