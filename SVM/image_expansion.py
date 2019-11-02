# -*- coding: utf-8 -*-
"""
Created on Fri May 31 09:53:20 2019

@author: lenovo
"""
# 当flipCode的值为 1 ：水平翻转；
# 当flipCode的值为 0 ：垂直翻转；
# 当flipCode的值为 -1 ：水平垂直翻转；
import cv2
from glob2 import glob

for fn in glob('*.jpg'): #确认文件格式
    img=cv2.imread(fn)
    horizontal_img=cv2.flip(img,1)
    vertical_img=cv2.flip(img,0)
    horver_img=cv2.flip(img,-1)
    splitName=fn.split(".")
    newName=splitName[0]
    cv2.imwrite(newName+'_hflip.jpg',horizontal_img)
    cv2.imwrite(newName+'_vflip.jpg',vertical_img)
    cv2.imwrite(newName+'_hvflip.jpg',horver_img)
    
        
