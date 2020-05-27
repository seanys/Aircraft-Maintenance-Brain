#-*- coding: utf-8 -*-
import fitz
import os
import re
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument


def getAMMChapters():
    path = os.path.abspath(os.path.join(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))), "..\\.."))
    ammPath = path+'\\Boeing-73NG Documents\\73NG-AMM_9309'
    outPath = path+'\\PDF and Search Algorithm\\PDF Process\\AMM Process'
    chapterFiles = os.listdir(ammPath)
    out = open(outPath+'\\'+'AMMchapters.csv', 'w', encoding='utf-8')
    for chapterFile in chapterFiles:
        fileID = chapterFile.split(' ')[0]
        index = createIndex(ammPath+'\\'+chapterFile)
        amm = open(ammPath+'\\'+chapterFile, 'rb')
        parser = PDFParser(amm)
        document = PDFDocument(parser)
        outlines = document.get_outlines()
        for (level, title, dest, a, se) in outlines:
            output = [fileID, str(level), title, str(index[dest[0].objid])]
            out.write('^'.join(output)+'\n')
        amm.close()
        print(str(fileID)+' OK.')
    out.close()

def createIndex(path):
    '''
    # 建立Xref的ID与页数的字典索引
    '''
    index = {}
    # 使用正则表达式来查找图片
    checkPage = r"/Type(?= */Page)"
    # 打开pdf
    doc = fitz.open(path)
    # 页面计数
    pagecount = 1
    lenXREF = doc ._getXrefLength()
    print("文件名:{}, 页数: {}, 对象: {}".format(path, len(doc), lenXREF - 1))
    # 遍历每一个对象
    for i in range(1, lenXREF):
        text = doc._getXrefString(i)            # 定义对象字符串
        isPage = re.search(checkPage, text)
        if isPage:
            pagecount += 1
        index[i] = pagecount
        if index[i] > len(doc):
            index[i] = 1
    return index


getAMMChapters()
