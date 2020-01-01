#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/30 0030  22:27
#Author:chao
import xlrd
import os
import xlwt
from testCase.test_case import myTestCase
readbook = xlrd.open_workbook(r'..\testData\data.xls')
file = xlwt.Workbook()
class writeExcle(object):
    def __init__(self):
        print("将实际结果和执行状态写入excel：")
    def write(self,result,status):
