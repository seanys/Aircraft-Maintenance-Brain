import numpy as np
import cv2
import os
import time
import re
import urllib.request

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

def getHist(img):
	image = cv2.resize(img,(960, 540), interpolation = cv2.INTER_CUBIC)
	hist = cv2.calcHist([image], [0, 1, 2], None, [4,4,4],[0, 256, 0, 256, 0, 256])
	hist = cv2.normalize(hist, hist, 0,255, cv2.NORM_MINMAX).flatten()
	return hist

if __name__ == '__main__':
	time1 = time.time()
	img_src="http://ww3.sinaimg.cn/large/006tNc79ly1g5vyegvol6j30by08qju7.jpg"
	resp = urllib.request.urlopen(img_src)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
		
	image_init = image
	hash1 = aHash(image_init)
	inhist = getHist(image_init)

	# root1 = '/Users/sean/Documents/MyProjects/Python/Image Recognition/data/compare/'
	root1 = '/data/release/api/image_color_similar.py'
	for subdir1, dirs1, files1 in os.walk(root1):
		files1.sort()
		for file1 in files1:
			if(re.search(r'(.png|.jpeg|.jpg)$',file1)!=None):
				
				pa1 = str(root1) + str(file1)
				image_compare = cv2.imread(pa1)
				hash2 = aHash(image_compare)

				nhist = getHist(image_compare)

				val = cv2.compareHist(inhist, nhist, 0)
				n = cmpHash(hash1, hash2)
				if (val>0.5 and n>0.7) or (val>0.7 and n>0.6):
					print(file1)
					print("色彩相似相关系数: ",val)
					print('均值哈希相似度：', n)
				# print("File Name: ",file1)
				# print("相似相关系数: ",val)
				# print('均值哈希算法相似度：', n)

	print("总耗时：",(time.time() - time1))