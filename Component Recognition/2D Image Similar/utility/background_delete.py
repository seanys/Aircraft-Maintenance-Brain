import cv2  
import numpy as np
img = cv2.imread('/Users/sean/Documents/MyProjects/Python/image/data/K218A004.png')  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                        #转换为灰度图像
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)        #转换为二值图像  

_, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#提取轮廓

cv2.drawContours(img,contours,-1,(0,0,255),2)  
cv2.imshow("img", img)  
cv2.waitKey(0)