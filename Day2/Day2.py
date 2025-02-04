# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:25:21 2019

@author: user
"""

#note
#HSB(Hue[色相],Saturation[飽和度],Brightness[明度]),HSV(Hue,Saturation,Value[明度]),
#HSL(Hue,Saturation,Lightness[亮度])

#HSB = HSV

#HSB
#Hue色相以360度決定顏色
#Saturtion飽和度以0~100%決定色彩純度,黑白灰色系飽和度為0
#Brightness明度以0~100%決定鮮豔程度,黑色明度為0

#HSL
#飽和度這邊有差別,HSB的0~100%為白色到選擇的色相;而HSL的0~100%是灰色到選擇的色相
#亮度的差別,HSB的明度是光的量，可以是任何顏色;HSL的亮度是白色的量


#LAB
#Lightness明亮度,0~100
#A顏色對立的維度,-128~127由小到大,由綠轉紅
#B顏色對立的維度,-128~127,由小到大,由藍轉黃

#BGR
#OpenCV預設的方式

#RGBA
#A以0~100表示不同的透明程度,數值越小越透明

#改變圖片的呈現
#cv2.cvtColor(Image,CODE)
#cv2.COLOR_BGR2HSV
#cv2.COLOR_BGR2HSL
#cv2.COLOR_BGR2LAB

#==============================================================

import cv2

img_path='D:\\1st-DL-CVMarathon\\1st-DL-CVMarathon\\Day2\\lena.png'

img = cv2.imread(img_path,1)
img_HLS = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
img_LAB = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)

while True:
    cv2.imshow('bgr',img) 
    cv2.imshow('HLS',img_HLS)
    cv2.imshow('LAB',img_LAB)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break

#cv2.waitKey(0) #waitkey作用為不斷刷新圖像，0代表顯示第一偵圖
#cv2.destroyAllWindows() #按下任意鍵關閉所有視窗


