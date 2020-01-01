#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/29 0029  16:50
#Author:chao
import requests
class configHttp(object):
    def __init__(self):
        print('开始请求接口')
    def get(self,url,param=None):
        result = requests.get(url=url,params=param).text
        return result
    def post(self,url,data=None):
        result = requests.put(url=url,data=data).text
        return result
    def requests(self,url,method,param=None):
        global result
        if method == 'get':
            result = self.get(url,param)
        elif method == 'post':
            result = self.post(url,param)
        else:
            print("请用‘get’或‘post’方法执行！")
        return result
