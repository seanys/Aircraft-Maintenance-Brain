# -*- coding: UTF-8 -*-
import camelot
import os


def getIPCtext(IPCpath, page):
    IPCpage = camelot.read_pdf(IPCpath, pages=str(page), columns=['157'],
                               flavor='stream', table_areas=['48,800,372,77'])
    result = IPCpage[0].data
    part = []
    description = ''
    catNo = ''
    price = ''
    qty = ''
    note = ''
    unit = ''
    flag0 = 0  # 1 Unit 2 Cat.No 3 Price
    flag1 = 0  # 1 Descripiton 2 Qty 3 Note
    pid = 0
    for line in result:
        if line[1] != '':
            if 'Description:' in line[1]:
                flag1 = 1
                flag0 = 1
                if description != '':
                    pid += 1
                    part.append([str(page), str(pid), unit, description,
                                 catNo, price, qty, note])
                    description = line[1].split('Description:')[1]
            elif 'Qty:' in line[1]:
                flag1 = 2
                qty = line[1].split('Qty:')[1]
            elif 'Note:' in line[1]:
                flag1 = 3
                note = line[1].split('Note:')[1]
            else:
                if flag1 == 1:
                    description += line[1]
                if flag1 == 2:
                    catNo += line[1]
                if flag1 == 3:
                    note += line[1]
        if line[0] != '':
            if 'Cat.' in line[0]:
                flag0 = 2
                catNo = line[0].replace('\n','').split('Cat.')[0]
            elif 'Price:' in line[0]:
                flag0 = 3
                price = line[0].split('Price:')[1]
            else:
                if flag0 == 1:
                    unit = line[0]
                if flag0 == 3:
                    price += line[0]
    # 添加最后一个零件
    pid += 1
    part.append([str(page), str(pid), unit, description, catNo, price, qty, note])
    return part


if __name__ == "__main__":
    path = os.path.abspath(os.path.join(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))), "..\\.."))
    IPCpath = path+'\\PDF and Search Algorithm\\IPC-Example\\Illustrated parts catalog.pdf'
    f = open(path+'\\PDF and Search Algorithm\\PDF Process\\IPC Process\\IPCtext.csv', 'w', encoding='utf-8')
    f.close()
    f = open(path+'\\PDF and Search Algorithm\\PDF Process\\IPC Process\\IPCtext.csv', 'a', encoding='utf-8')
    for i in range(7, 36):
        partList=getIPCtext(IPCpath, i)
        for part in partList:
            f.write(','.join(part).replace('\n','')+'\n')
        print('Page'+str(i)+' OK.')
    f.close()