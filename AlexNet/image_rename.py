# -*- coding: utf-8 -*-
"""
Created on Fri May 31 09:07:40 2019

@author: lenovo
"""
#给图片名字加标签
import cv2
import os
# 不要用中文路径
# 训练集改名
# =============================================================================
hurtnum=0
mildewnum=0
wormnum=0
dir='./train/'
for root, dirs, files in os.walk(dir):
     for file in files:
         filepath = os.path.join(root, file) 
         image = cv2.imread(filepath)
         if 'hurt' in file:
             file='hurt.'+str(hurtnum)+'.jpg'
             hurtnum+=1
         if 'mildew' in file:
             file='mildew.'+str(mildewnum)+'.jpg'
             mildewnum+=1
         if 'worm' in file:
             file='worm.'+str(wormnum)+'.jpg'
             wormnum+=1
         path = './train/'+file
         cv2.imwrite(path,image)
      
     cv2.waitKey(0)
# =============================================================================
# 测试集改名
imgnum=0
dir='./test/'
for root, dirs, files in os.walk(dir):
    for file in files:
        filepath = os.path.join(root, file) 
        image = cv2.imread(filepath)       
        file=str(imgnum)+'.jpg'
        imgnum+=1
        path = './test/'+file
        cv2.imwrite(path,image)
     
    cv2.waitKey(0)