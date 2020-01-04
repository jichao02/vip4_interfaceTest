#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/29 0029  16:50
#Author:chao
import requests,json
class configHttp(object):
    def __init__(self):
        print('开始请求接口')
    def get(self,url,param=None):
        result = requests.get(url=url,params=param)
        # 转换成dict格式
        dict = json.loads(result.text)
        # 拿到errorcode对应的值
        result = dict["errorCode"]
        return result
    def post(self,url,data=None):
        result = requests.post(url=url,data=eval(data))
        dict = json.loads(result.text)
        result = dict["errorCode"]
        return result
    def requests(self,url,method,param=None):
        global result
        if method == 'get' or method == "GET":
            result = self.get(url,param)
        elif method == 'post' or method == "POST":
            result = self.post(url,param)
        else:
            print("请用‘get’或‘post’方法执行！")
        return result
if __name__ == '__main__':
    a = configHttp()
    b = a.requests("https://www.wanandroid.com/user/logout/json","GET","{'username':'liangchao'}")
    print(b)