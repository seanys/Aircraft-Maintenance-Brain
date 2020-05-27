
import cv2
import numpy as np
import time
#均值哈希算法
def aHash(img):
    #缩放为8*8
    img=cv2.resize(img,(8,8),interpolation=cv2.INTER_CUBIC)
    #转换为灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #s为像素和初值为0，hash_str为hash值初值为''
    s=0
    hash_str=''
    #遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s=s+gray[i,j]
            #求平均灰度
    avg=s/64
    #灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if gray[i,j]>avg:
                hash_str=hash_str+'1'
            else:
                hash_str=hash_str+'0'
    return hash_str

#Hash值对比
def cmpHash(hash1,hash2):
    n=0
    #hash长度不同则返回-1代表传参出错
    if len(hash1)!=len(hash2):
        return -1
    #遍历判断
    for i in range(len(hash1)):
    #不相等则n计数+1，n最终为相似度
        if hash1[i]!=hash2[i]:
            n=n+1
    return 1 - n / 64
 
def hammingDist(s1, s2):
#assert len(s1) == len(s2)
    return 1 - sum([ch1 != ch2 for ch1, ch2 in zip(s1, s2)])*1. / (32*32/4)
 
if __name__ == '__main__':
    img1 = cv2.imread("/Users/sean/Documents/MyProjects/Python/image/data/IMG_0314.jpeg")
    img2 = cv2.imread("/Users/sean/Documents/MyProjects/Python/image/data/IMG_0315.jpeg")
    time1 = time.time()
    hash1 = aHash(img1)
    hash2 = aHash(img2)
    n = cmpHash(hash1, hash2)
    print('均值哈希算法相似度：', n, "-----time=", (time.time() - time1))