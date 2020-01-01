#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/29 0029  15:22
#Author:chao
import unittest
from ddt import ddt,data,unpack,file_data
from common.readExcel import readExcel
from common.configHttp import configHttp
'''
1、导入目标模块或包
2、调用readExcel模块，获取测试数据
3、根据测试数据，调用对应的接口方法，完成接口请求
4、获取实际结果
5、将实际结果和预期结果进行比对
6、将接口执行状态写入excel
'''
da = readExcel()
test_data = da.getRequests()
print(test_data)
@ddt
class myTestCase(unittest.TestCase):
    @data(*test_data)
    @unpack
    def send_request(self,id,url,name,method,param,expect):
        print(id,url,name,method,param,expect)
        c = configHttp()
        request = c.requests(url,method,param)
        print("接口请求完成")
if __name__ == '__main__':
    r = myTestCase()
    r.send_request(*test_data)








