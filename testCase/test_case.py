#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/29 0029  15:22
#Author:chao
# 1、导入目标模块或包
import unittest,json
from ddt import ddt,data,unpack
from common.readExcel import readExcel
from common.configHttp import configHttp
from common.writeExcel import writeExcel
# 2、调用readExcel模块，获取测试数据
da = readExcel()
wr = writeExcel()
test_data = da.getRequests()
@ddt
class myTestCase(unittest.TestCase):
    @ddt
    @data(*test_data)
    @unpack
    def test_request(self,id,url,name,method,param,expect):
        # print(id,url,name,method,param,expect)
        # 处理数据格式，取每一个的第一个
        param = param[0]
        expect = expect[0]
        # 3、根据测试数据，调用对应的接口方法，完成接口请求
        # 4、获取实际结果
        c = configHttp()
        result = c.requests(url,method,param)
        try:
            # 5、将实际结果和预期结果进行比对
            self.assertEqual(str(result), str(expect))
            status = "Success"
        except AssertionError as msg:
            print(msg)
            status = 'Fail'
            # 6、将接口执行状态写入excel
        real = result
        wr.writeExcel(int(id), real, status)
if __name__ == '__main__':
    unittest.main()









