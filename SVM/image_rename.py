# -*- coding: utf-8 -*-
"""
Created on Fri May 31 09:07:40 2019

@author: lenovo
"""
#给图片名字加标签
import cv2
import os
# 不要用中文路径

dir='./image_data/hurt/'
for root, dirs, files in os.walk(dir):
    for file in files:
        filepath = os.path.join(root, file) 
        image = cv2.imread(filepath)
        file='hurt'+file
        path = './image_data/hurt/'+file
        cv2.imwrite(path,image)
     
    cv2.waitKey(0)


dir='./image_data/worm/'
for root, dirs, files in os.walk(dir):
    for file in files:
        filepath = os.path.join(root, file) 
        image = cv2.imread(filepath)
        file='worm'+file
        path = './image_data/worm/'+file
        cv2.imwrite(path,image)
     
    cv2.waitKey(0)



dir='./image_data/mildew/'
for root, dirs, files in os.walk(dir):
    for file in files:
        filepath = os.path.join(root, file)
        image = cv2.imread(filepath)
        file='mildew'+file
        path = './image_data/mildew/'+file
        cv2.imwrite(path,image)
     
    cv2.waitKey(0)
