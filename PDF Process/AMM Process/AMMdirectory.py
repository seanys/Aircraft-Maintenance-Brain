# -*- coding: UTF-8 -*-
import camelot
import os


def getAMM():
    # 获取手册路径及csv目录
    path = os.path.abspath(os.path.join(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))), ".."))
    csvPath = path+'\\PDF and Search Algorithm\\PDF Process'
    ammPath = path+'\\Boeing-73NG Documents\\737NG AMM 目录.pdf'

    # 从目录PDF文件中提取表格
    # 第一页指定表格区域，其余页不指定
    amm = camelot.read_pdf(
        ammPath, pages='1', table_areas=['0,480,790,0'], strip_text='\n')
    page = 1
    amm[0].to_csv(csvPath+'\\AMM\\p'+str(page)+'.csv')
    try:
        while True:
            amm = camelot.read_pdf(
                ammPath, pages=str(page), strip_text='\n')
            amm[0].to_csv(csvPath+'\\AMM\\p'+str(page)+'.csv')
            print(page)
            page = page+1
    except:
        print('OK')


def mergeAMM():
    # 获取csv目录
    path = os.path.abspath(os.path.join(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))), ".."))
    path = path+'\\PDF and Search Algorithm\\PDF Process'
    csvFiles = os.listdir(path)

    # 合并csv文件
    f = open(path+'\\AMMdirectory.csv', 'w', encoding='utf-8')
    for csvFile in csvFiles:
        csv = open(path+'\\'+csvFile, 'r', encoding='utf-8')
        lines = csv.readlines()
        for line in lines:
            line = line.replace('\n', '').split('"TASK ')[1].replace('"', '')
            if line == '':
                continue
            f.write(line+'\n')
        csv.close()
    f.close()


def getFooter():
    # 获取页码信息
    path = os.path.abspath(os.path.join(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))), ".."))
    csvPath = path+'\\PDF and Search Algorithm\\PDF Process\\Footer'
    path = path+'\\Boeing-73NG Documents\\73NG-AMM_9309'
    chapterFiles = os.listdir(path)
    for chapterFile in chapterFiles:
        fileID = chapterFile.split(' ')[0]
        done=['05','06'] # 已完成列表
        if fileID in done:
            continue
        print(fileID+' started.')
        try:
            page = 2  # 跳过封面
            while True:
                f = open(csvPath+'\\'+fileID+'.csv', 'a', encoding='utf-8')
                footer = camelot.read_pdf(
                    path+'\\'+chapterFile, pages=str(page), flavor='stream', table_areas=['330,120,560,0'])
                data = footer[0].data
                output = []
                try:
                    output.append(fileID)
                    output.append(page)
                    output.append(data[0][len(data[0])-1])
                    output.append(data[1][len(data[1])-1].split(' ')[1])
                    output.append(
                        data[2][len(data[2])-1].split('/')[0].split(' ')[0])
                    output.append(
                        data[2][len(data[2])-1].split('/')[0].split(' ')[1])
                    output.append(data[2][len(data[2])-1].split('/')[1])
                    f.write(str(output).replace(
                        '[', '').replace(']', '').replace("'", '')+'\n')
                    #输出示例 05, 2, 05-EFFECTIVE PAGES, 1, Nov, 09, 2018
                    #输出说明 文档号, 实际页码, 章节名, 标定页码, 月份, 日期, 年份
                except:
                    print('No page.')
                    f.write(fileID+', '+str(page) +
                            ', NULL, NULL, NULL, NULL, NULL\n')
                finally:
                    print(page)
                    f.close()
                    page = page+1
        except:
            print(fileID+' completed.')


def getContent():
    path = os.path.abspath(os.path.join(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))), ".."))
    cPath = path+'\\PDF and Search Algorithm\\PDF Process\\Content'
    fPath = path+'\\PDF and Search Algorithm\\PDF Process\\Footer'
    path = path+'\\Boeing-73NG Documents\\73NG-AMM_9309'
    chapterFiles = os.listdir(path)
    for chapterFile in chapterFiles:
        fileID = chapterFile.split(' ')[0]
        fcsv = open(fPath+'\\'+fileID+'.csv', 'r', encoding='utf-8')
        ccsv = open(cPath+'\\'+fileID+'.csv', 'w', encoding='utf-8')
        chapter = ''
        page_show = ''
        for line in fcsv.readlines():
            print(line)
            if len(line)>0 and line.split(',')[2].split('-')[1]=='CONTENTS':
                page=line.split(',')[1]
                print(page)
                content = camelot.read_pdf(
                    path+'\\'+chapterFile, pages=page, flavor='stream', table_areas=['0,680,560,117'])
                print(content[0].df)
                for item in content[0].data:
                    output = []
                    if len(item[1]) != 0:
                        chapter = item[1]
                    if len(item[2]) != 0:
                        page_show = item[2]
                    if 'TASK' in item[0]:
                        output.append(item[0])
                        output.append(chapter)
                        output.append(page_show)
                        print(output)

getAMM()
# # 可视化分析表格区域
# # plt = camelot.plot(tables[0], kind='text')
# # plt.show()
