# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 00:21:42 2019

@author: user
"""

#note

#水平與垂直翻轉 (flip)

#縮放(scale)
#cv2.resize(img,new_img_shape,fx,fy,interpolation)
#new_img_shape 跟 fx,fy 選擇其中一種方式表示

#interpolation:處理方式，會影響處理的速度與品質
#cv2.INTER_NEAREST: 最鄰近插點法
#cv2.INTER_LINEAR: 雙線性插補(預設)
#cv2.INTER_AREA: 臨域像素再取樣插補
#cv2.INTER_CUBIC: 雙立方插補，4×4大小的補點
#cv2.INTER_LANCZOS4: Lanczos插補，8×8大小的補點

#預設縮放接皆用INTER_LINEAR
#建議縮小用 INTER_AREA
#建議放大用 INTER_CUBIC (slow) 或是 INTER_LINEAR


#平移操作
#兩種方式，一為手動作xy軸的四則運算,二為以矩陣運算方式操作 (快)



#OpenCV實務上提供一個廣泛的變換函數
#cv2.wrapAffine(img,Matrix,(column,row))
#透過np.array產生平移矩陣
#透過wrapAffine產生平移後圖片




#HW

import cv2
import numpy as np

img_path = 'D:\\1st-DL-CVMarathon\\1st-DL-CVMarathon\\Day4\\lena.png'
img = cv2.imread(img_path,1)

'''

#cv2.imshow('img',img)

#上下翻轉
img_ver_rotate = img[::-1,:,:]
#cv2.imshow('img_ver_rotate',img_ver_rotate)

#拼湊
img_imgVer = np.vstack((img,img_ver_rotate))

#左右翻轉
img_imgVer_hor_rotate = img_imgVer[:,::-1,:]

#拼湊
img_imgVer_imgHor = np.hstack((img_imgVer_hor_rotate,img_imgVer))


img_test = cv2.resize(img_imgVer_imgHor,None,fx=0.5,fy=0.5)


while True:
    cv2.imshow('img_imgVer',img_imgVer)
    cv2.imshow('img_test',img_test)
    k=cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break
'''


##比較鄰近差值 與 雙立方差值

img_shrink = cv2.resize(img,None,fx=0.2,fy=0.2,interpolation=cv2.INTER_AREA)
#cv2.imshow('img_shrink',img_shrink)

fx , fy =5 , 5

#INTER_NEAREST

img_Nearest = cv2.resize(img_shrink,None,fx=fx,fy=fy,interpolation = cv2.INTER_NEAREST)

#Original
img_Ori = cv2.resize(img,img_Nearest.shape[:2])


#Combine
img_Nearest_Ori = np.hstack((img_Nearest,img_Ori))

cv2.imshow('img_Nearest_Ori',img_Nearest_Ori)

cv2.waitKey(0)
cv2.destroyAllWindows()



##平移練習

#練習平移X 100 pixel ;y 50 pixel

M = np.array([[1,0,100],
             [0,1,50]],dtype=np.float32)
#第一行為移動x方向,第一欄為1,第3位為距離
#第二行為移動y方向,第二欄為1,第3位為距離

img_shift = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))

img_imgShift = np.hstack((img,img_shift))

cv2.imshow('img_imgShift',img_imgShift)

cv2.waitKey(0)
cv2.destroyAllWindows()



