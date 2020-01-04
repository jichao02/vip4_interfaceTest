#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/1/1 0001  20:36
#Author:chao
'''
1、导入包
2、创建对象
3、读取内容
4、关闭
'''
import os
import configparser
# 取上一层目录
path = os.path.dirname(__file__)
# 再取上一层目录
path = os.path.dirname(path)
print(path)
# 拼接要读取的目录
new_path = os.path.join(path,"config.ini")
print(new_path)
class readConfig(object):
    def __init__(self):
        # 进行实例化
        self.config = configparser.ConfigParser()
        # 读取路径和声明编码格式
        self.config.read(new_path,encoding='utf-8')
    def getEmail(self,name):
        # 用get方法获取对应的内容
        value = self.config.get('EMAIL',name)
        return value
if __name__ == '__main__':
    readConfig = readConfig()
    print("邮箱的名字是：",readConfig.getEmail('name'))
