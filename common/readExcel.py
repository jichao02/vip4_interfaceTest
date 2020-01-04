#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/29 0029  10:44
#Author:chao

# 1、导入读取excel的包
import xlrd
class readExcel(object):
    def __init__(self):
        # 2、打开目标文件
        readbook = xlrd.open_workbook(r'..\testData\data.xls')  # r解决路径名称问题
        # 3、定位sheet,并读取行数
        self.urlSheet = readbook.sheet_by_name('urlSheet')
        self.urlnum = self.urlSheet.nrows
        self.paramSheet = readbook.sheet_by_name('paramSheet')
        self.paramnum = self.paramSheet.nrows
        self.assertSheet = readbook.sheet_by_name('assertSheet')
        self.assertnum = self.assertSheet.nrows
    def getSheetData(self,num,sheetName):
        # 4、定位行和列（从哪一行那一列读取）
        data = []
        for i in range(1,num):
            # 循环体
            assertdata = sheetName.row_values(i)
            data.append(assertdata)
        return data
        # 6、组装数据
    def getRequests(self):
        # 5、调用获取sheet页数据的方法
        urlList = self.getSheetData(self.urlnum, self.urlSheet)
        paramList = self.getSheetData(self.paramnum, self.paramSheet)
        assertList = self.getSheetData(self.assertnum, self.assertSheet)
        dataList = []
        for i in range(len(urlList)):
            new_url = urlList[i]
            new_url.append(paramList[i][1:])
            new_url.append(assertList[i][1:])
            dataList.append(new_url)
        # 7、return给需要数据的地方
        return dataList

if __name__ == '__main__':
    getdata = readExcel()
    print(getdata.getRequests())
