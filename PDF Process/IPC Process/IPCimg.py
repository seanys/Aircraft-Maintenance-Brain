# -*- coding: UTF-8 -*-
import fitz
import time
import re
import os
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTFigure
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from PIL import Image


class GetPic:
    def __init__(self, filename, password=''):
        """
        初始化
        :param filename: pdf路径
        :param password: 密码
        """
        with open(filename, 'rb') as file:
            # 创建文档分析器
            self.parser = PDFParser(file)
        # 创建文档
        self.doc = PDFDocument()
        # 连接文档与文档分析器
        self.parser.set_document(self.doc)
        self.doc.set_parser(self.parser)
        # 初始化, 提供初始密码, 若无则为空字符串
        self.doc.initialize(password)
        # 检测文档是否提供txt转换, 不提供就忽略, 抛出异常
        if not self.doc.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            # 创建PDF资源管理器, 管理共享资源
            self.resource_manager = PDFResourceManager()
            # 创建一个PDF设备对象
            self.laparams = LAParams()
            self.device = PDFPageAggregator(
                self.resource_manager, laparams=self.laparams)
            # 创建一个PDF解释器对象
            self.interpreter = PDFPageInterpreter(
                self.resource_manager, self.device)
            # pdf的page对象列表
            self.doc_pdfs = list(self.doc.get_pages())
        #  打开PDF文件, 生成一个包含图片doc对象的可迭代对象
        self.doc_pics = fitz.open(filename)

    def to_pic(self, doc, zoom, pg, pic_path):
        """
        将单页pdf转换为pic
        :param doc: 图片的doc对象
        :param zoom: 图片缩放比例, type int, 数值越大分辨率越高
        :param pg: 对象在doc_pics中的索引
        :param pic_path: 图片保存路径
        :return: 图片的路径
        """
        rotate = int(0)
        trans = fitz.Matrix(zoom, zoom).preRotate(rotate)
        pm = doc.getPixmap(matrix=trans, alpha=False)
        path = os.path.join(pic_path, str(pg)) + '.png'
        pm.writePNG(path)
        return path

    def get_pic_loc(self, doc):
        """
        获取单页中图片的位置
        :param doc: pdf的doc对象
        :return: 返回一个list, 元素为 [图片名称,应截取的区域],当前页的尺寸
        """
        self.interpreter.process_page(doc)
        layout = self.device.get_result()
        # pdf的尺寸, tuple, (width, height)
        canvas_size = layout.bbox
        # 图片名称与应截取的区域
        loc_named_pic = []
        # 遍历单页的所有LT对象
        rank = 0
        for x in layout:
            if isinstance(x, LTFigure):
                # matrix的格式猜测为(w, ?, ?, h, x, y)
                loc_named_pic.append([rank, x.matrix])
                rank += 1
        return loc_named_pic, canvas_size

    def get_crops(self, pic_path, canvas_size, position, cropped_pic_name, cropped_pic_path):
        """
        按给定位置截取图片
        :param pic_path: 被截取的图片的路径
        :param canvas_size: 图片为pdf时的尺寸, tuple, (0, 0, width, height)
        :param position: 要截取的位置, tuple, (w, ?, ?, h, x, y)
        :param cropped_pic_name: 截取的图片名称
        :param cropped_pic_path: 截取的图片保存路径
        :return:
        """
        img = Image.open(pic_path)
        print(position)
        # 当前图片的尺寸 tuple(width, height)
        pic_size = img.size
        x1 = pic_size[0] * (position[4]/canvas_size[2])
        x2 = pic_size[0] * ((position[4]+position[0])/canvas_size[2])
        y1 = pic_size[1] * (1-(position[5]+position[3])/canvas_size[3])
        y2 = pic_size[1] * (1-position[5]/canvas_size[3])
        cropped_img = img.crop((x1, y1, x2, y2))
        # 保存截图文件的路径
        path = os.path.join(cropped_pic_path, cropped_pic_name) + '.png'
        cropped_img.save(path)
        print('成功截取图片:', cropped_pic_name)

    def main(self, pagePath, picOldPath, picPath, pgn=None):
        """
        主函数
        :param pagePath: 被截取的图片路径
        :param picOldPath: fitz库提取出的图片路径
        :param picPath: 最终图片路径
        :param pgn: 指定获取截图的对象的索引（从0开始）
        :return:
        """

        if pgn is not None:
            page = pgn+1  # page从1开始，pgn从0开始
            # 获取当前页的doc
            doc_pdf = self.doc_pdfs[pgn]
            loc_name_pic, canvas_size = self.get_pic_loc(doc_pdf)
            if loc_name_pic:
                rank = []
                loc_name_pic.sort(key=lambda pic: pic[1][5], reverse=True)
                for i in loc_name_pic:
                    rank.append(i[0])
                print(page, rank)
            if self.numberJudge(picOldPath, page, len(rank)) == True:  # 图片数量是否正常
                for i in range(len(rank)):
                        copy(picOldPath+'\\{}-{}.png'.format(str(page), str(rank[i]+1)),
                             picPath+'\\{}-{}.png'.format(str(page), str(i+1)))
            else:
                print(str(page)+' 手动截图')
                doc_pic = self.doc_pics[pgn]
                # 将当前页转换为PNG, 返回值为图片路径
                path = self.to_pic(doc_pic, 6, pgn, pagePath)
                # 手动控制截图区域
                picID = 1
                for i in range(0, 6):
                    position = 164, 0, 0, 119, 371, 674-119*i
                    cropped_pic_name = str(page)+'-'+str(picID)
                    picID += 1
                    self.get_crops(path, canvas_size, position,
                                   cropped_pic_name, picPath)

            # 根据排序自动截图
            # for i in loc_name_pic:
            #     position = i[1]
            #     cropped_pic_name = re.sub(
            #         '/', '_', str(pgn)+'-'+str(picID))
            #     picID += 1
            #     self.get_crops(path, canvas_size, position,
            #                    cropped_pic_name, cropped_pic_path)

    def numberJudge(self, picOldPath, page, number):  # 判断某页图片数量是否正常
        for i in range(0, number):
            if os.path.exists(picOldPath+'\\{}-{}.png'.format(str(page), str(i+1))) == False:
                return False
        if os.path.exists(picOldPath+'\\{}-7.png'.format(str(page))) == True:
            return False
        else:
            return True


def pdf2png(path, pic_path):
    '''
    # 从pdf中提取图片
    :param path: pdf的路径
    :param pic_path: 图片保存的路径
    :return:
    '''
    # 使用正则表达式来查找图片
    checkXO = r"/Type(?= */XObject)"
    checkIM = r"/Subtype(?= */Image)"
    checkPage = r"/Type(?= */Page)"
    # 打开pdf
    doc = fitz.open(path)
    # 页面计数
    pagecount = -1
    lenXREF = doc ._getXrefLength()
    # 打印PDF的信息
    print("文件名:{}, 页数: {}, 对象: {}".format(path, len(doc), lenXREF - 1))
    # 遍历每一个对象
    for i in range(1, lenXREF):
        text = doc._getXrefString(i)            # 定义对象字符串
        isPage = re.search(checkPage, text)
        if isPage:
            pagecount += 1
            # 页面内图片计数
            imgcount = 0
        if pagecount not in pageRange:          # 页码区间根据实际修改，区间为左闭右开
                continue
        isXObject = re.search(checkXO, text)    # 使用正则表达式查看是否是对象
        isImage = re.search(checkIM, text)      # 使用正则表达式查看是否是图片
        if not isXObject or not isImage:        # 如果不是对象也不是图片，则continue
            continue
        imgcount += 1
        pix = fitz.Pixmap(doc, i)               # 生成图像对象
        new_name = "{}-{}.png".format(pagecount, imgcount)  # 生成图片的名称
        if pix.n < 5:                           # 如果pix.n<5,可以直接存为PNG
            pix.writePNG(os.path.join(pic_path, new_name))
        else:                                   # 否则先转换CMYK
            pix0 = fitz.Pixmap(fitz.csRGB, pix)
            pix0.writePNG(os.path.join(pic_path, new_name))
            pix0 = None
        pix = None                              # 释放资源


def copy(path1, path2):
    f1 = open(path1, 'rb')
    f2 = open(path2, 'wb')
    for i in f1:
        f2.write(i)
    f1.close()
    f2.close()


def sortPic(IPCpath, path):
    getPic = GetPic(IPCpath)
    pagePath = path+'\\PDF and Search Algorithm\\PDF Process\\IPC Process\\page'
    picPath = path+'\\PDF and Search Algorithm\\PDF Process\\IPC Process\\pic'
    picOldPath = path+'\\PDF and Search Algorithm\\PDF Process\\IPC Process\\pic_old'
    for i in pageRange:
        getPic.main(pagePath, picOldPath, picPath, pgn=i-1)


if __name__ == '__main__':
    path = os.path.abspath(os.path.join(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))), "..\\.."))
    IPCpath = path+'\\PDF and Search Algorithm\\IPC-Example\\Illustrated parts catalog.pdf'
    pngpath = path+'\\PDF and Search Algorithm\\PDF Process\\IPC Process\\pic_old'
    pageRange = range(7, 36)  # 页码区间根据实际修改，区间为左闭右开，从1开始
    pdf2png(IPCpath, pngpath)
    sortPic(IPCpath, path)
