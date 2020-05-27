import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/sean/Documents/MyProjects/Python/image/data/1U8102.png')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.show()