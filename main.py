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
class run_all(object):
    def run_case(self):
        case_path = os.getcwd()+"\\"+"testCase"
        # 找到所有的测试用例--discover
        discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py', top_level_dir=None)
        return discover
    def clear_report(self):
        nowPath = os.path.dirname(__file__)
        print('nowpath', nowPath)
        reportPath = nowPath + "/" + "testReport"
        fileList = os.listdir(reportPath)
        # 如果该目录下的文件超过5个，则开始清理
        if len(fileList) > 5:
            for i in fileList:
                file = reportPath + "/" + i
                os.remove(file)

        fileNewList = os.listdir(reportPath)
        print(fileNewList)
if __name__ == '__main__':
    r = run_all()
    r.clear_report()
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.getcwd() + "\\testReport\\" + current_time + '.html'
    file = open(report_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,title="自动化测试报告",description="测试报告描述",verbosity=2)
    runner.run(r.run_case())
    file.close()
    c = sendEmail()
    c.send_email()