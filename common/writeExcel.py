#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/30 0030  22:27
#Author:chao
import xlrd
import os
from xlutils.copy import copy
class writeExcel(object):
    dir = 'testData'
    excel_dir = os.path.dirname(os.getcwd()) + "\\" + dir
    excel_dir = os.getcwd() + "\\" + dir
    print('excel_dir', excel_dir)
    rb = xlrd.open_workbook(excel_dir + '\\' + 'data.xls')
    wb = copy(rb)
    # 通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(2)
    def __init__(self):
        print("将实际结果和执行状态写入excel：")
    def writeData(self, id, real, status):
        try:
            print('写入')
            # 根据id写入对应的实际结果和接口测试状态
            self.ws.write(id, 2, real)
            self.ws.write(id, 3, status)
            self.wb.save(self.excel_dir + '\\' + 'data.xls')
            return 'ok'
        except Exception as msg:
            print(msg)