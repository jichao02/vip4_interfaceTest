#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/29 0029  10:43
#Author:chao
'''
1-找到所有测试用例--discover
2-运行测试用例并生成报告
3-关闭报告
4-调用邮件模块，发送邮件
'''
import unittest
import time,os
import now
import HTMLTestRunner
from common.sendEmail import sendEmail

def run_case(self):
    case_path = os.getcwd()+"\\"+"testCase"
    # 找到所有的测试用例--discover
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_case*.py', top_level_dir=None)
    return discover

if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.getcwd() + "\\testReport\\" + current_time + '.html'
    file = open(report_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,title="自动化测试报告",description="测试报告描述",verbosity=2)
    runner.run(run_case())
    file.close()
    c = sendEmail()
    c.send_email()