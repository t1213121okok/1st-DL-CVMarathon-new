# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:53:28 2019

@author: user
"""
#note

#通常稱呼RGB各為一個channel
#用img[:,:,0],[:,:,1],[:,:,2] 取得不同channel的row column值
#有一個option寫法: img[...,1]

#特別注意
#OpenCV會以0~255的值表示,有些值會以百分比或含負值的方式
#OpenCV顯示圖片會以unit8(可存範圍0~255)方式表示,如果計算過程中含負數或小數,得自己轉換




#範例 -- 調整飽和度
#轉換color space BRG->HSV

'''

import cv2
img_path = 'D:\\1st-DL-CVMarathon\\1st-DL-CVMarathon\\Day3\\lena.png'
img = cv2.imread(img_path,1)

img_hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)


#操作飽和度須轉為百分比(小數點)
img_hsv = img_hsv.astype('float32')

#降低兩成飽和度,得除以255
img_hsv[...,1] = img_hsv[...,1]/225 - 0.2

#再將圖片依序轉回255 --> uint8格式 --> BGR格式


img_hsv[...,1] = img_hsv[...,1]*225
img_hsv = img_hsv.astype('uint8')
img_hsv = cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR)

cv2.imshow('SHOW',img_hsv)



cv2.waitKey(0) #waitkey作用為不斷刷新圖像，0代表顯示第一偵圖
cv2.destroyAllWindows() #按下任意鍵關閉所有視窗
'''


#值方圖對比 - 當我們想增強對比的時候，可以考慮使用直方圖均衡的方式
#對比不強: 顏色的值集中在某個區域
#增強對比: 透過數學公式將值分散到0~255

'''
import cv2

img_path = 'D:\\1st-DL-CVMarathon\\1st-DL-CVMarathon\\Day3\\lena.png'
img = cv2.imread(img_path,0)    #直方圖均衡一般處理灰圖,所以屬性設0
eq = cv2.equalizeHist(img)

cv2.imshow('img',img)
cv2.imshow('eq',eq)



cv2.waitKey(0) #waitkey作用為不斷刷新圖像，0代表顯示第一偵圖
cv2.destroyAllWindows() #按下任意鍵關閉所有視窗
'''

#如果處理RGB圖通常是會轉成HSV圖，在對明亮度做調整
#不過也可以個別對RGB三個channel做直方圖均衡


#也可以透過手動調整，以簡單的乘法和加法來改變
#實作
#for b in range(img.shape[0]):
#   for g in range(img.shape[1]):
#       for r in range(img.shape[2]):
#           透過np.clip限制範圍在0~225
#           img[b,g,r] = np.clip(alpha * img[b,g,r] + beta , 0 , 255)

#或是透過OpenCV內建function來做
#img = cv2.convertScaleAbs(img,alpha = a, beta = b)


import cv2
import numpy as np

#讀取圖片,並轉化為HSV格式
img_path = 'D:\\1st-DL-CVMarathon\\1st-DL-CVMarathon\\Day3\\lena.png'
img = cv2.imread(img_path,1)
#cv2.imshow('origin',img)

img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
change_ratio = 0.2

#降低對比

img_hsv_down = img_hsv.astype('float32')
img_hsv_down[..., 1] = img_hsv_down[..., 1] / 255 - change_ratio
img_hsv_down[..., 1] = img_hsv_down[..., 1] * 255
img_hsv_down = img_hsv_down.astype('uint8')

#身高對比
img_hsv_up = img_hsv.astype('float32')
img_hsv_up[...,1] = img_hsv_up[...,1]/255 + change_ratio
img_hsv_up[...,1] = img_hsv_up[...,1]*255
img_hsv_up = img_hsv_up.astype('uint8')



#轉換回去
img_hsv_down = cv2.cvtColor(img_hsv_down,cv2.COLOR_HSV2BGR)
img_hsv_up = cv2.cvtColor(img_hsv_up,cv2.COLOR_HSV2BGR)





#cv2.imshow('img_d',img_hsv_down)
#cv2.imshow('img_u', img_hsv_up)

img_all = np.hstack((img,img_hsv_down,img_hsv_up))
#cv2.imshow('all',img_all)

#cv2.imshow('pic',img)


while True:
    cv2.imshow('img_combine', img_all)
    
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break

#cv2.waitKey(0) #waitkey作用為不斷刷新圖像，0代表顯示第一偵圖
#cv2.destroyAllWindows() #按下任意鍵關閉所有視窗


#直方圖均衡

img_gray = cv2.imread(img_path,0)
img_gray_equ = cv2.equalizeHist(img_gray)
#cv2.imshow('gray',img_gray_equ)

img_gray_combine = np.hstack((img_gray,img_gray_equ))
#cv2.imshow('gray',img_gray_combine)

while True:
    cv2.imshow('img_gray_combine', img_gray_combine)
    
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break



#調整對比/明亮
#alpha控制對比:1~3  beta控制亮度:0~255
    
img_add_contrast = cv2.convertScaleAbs(img,alpha=2,beta=0)
img_add_bright = cv2.convertScaleAbs(img,alpha=1,beta=50)

img_contrast_bright = np.hstack((img_add_bright,img_add_contrast))

while True:
    cv2.imshow('img_contrast_bright', img_contrast_bright)
    
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break

