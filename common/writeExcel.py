#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/30 0030  22:27
#Author:chao
import xlrd
import os
from xlutils.copy import copy
class writeExcel(object):
    wb = xlrd.open_workbook(r"../testData/data.xls")
    wb = copy(wb)
    # 通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(2)
    def __init__(self):
        print("将实际结果和执行状态写入excel：")
    def writeExcel(self, id, real, status):
        try:
            # 根据id写入对应的实际结果和接口测试状态
            self.ws.write(id,2,real)
            self.ws.write(id,3,status)
            self.wb.save(r"../testData/data.xls")
            return "ok"
        except Exception as msg:
            print(msg)
if __name__ == '__main__':
    w = writeExcel()
    w.writeExcel(4,4,7)