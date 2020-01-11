#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/1/4 0004  17:47
#Author:chao
import smtplib,os,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.readConfig import readConfig
from email.header import Header

class sendEmail(object):
    # 读取ini文件配置属性
    r = readConfig()
    host = r.getEmail('mail_host')
    # 配置第三方SMTP服务
    mail_host = "smtp.163.com"   # 设置服务器
    mail_port = r.getEmail('mail_port')
    mail_user = r.getEmail('mail_user')
    mail_pass = r.getEmail("mail_pass")
    # 配置邮件属性
    sender = r.getEmail("sender")
    receiver = r.getEmail("receiver")
    content = r.getEmail("content")
    # t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 查找目录下的最新文件
    def find_file(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        # 获取报告的存放路径
        report_path = os.path.dirname(current_path) + "/" + 'testReport'
        # 获取存放路径下的全部文件名称的列表
        file_list = os.listdir(report_path)
        fileDict = {}
        fileTime = []
        for iName in file_list:
            # 拼接文件路径和i文件名
            filename = report_path + "/" + iName
            # 获取该文件的修改时间
            iTime = os.path.getatime(filename)
            # 将该文件的修改时间追加都时间列表中
            fileTime.append(iTime)
            # 将文件的修改时间itime作为key,文件名iname作为字典的value存入
            fileDict[iTime] = iName
        sendfile = fileDict[max(fileTime)]
        # 拼接最新文件的路径
        send_file = report_path + "/" + sendfile
        return sendfile
    # 配置邮件属性
    def config_mail(self):
        send_file = self.find_file()
        send_file = open(send_file,'rb').read()
        # 组装邮件内容和标题，中文需参数’utf-8‘，单字节字符不需要
        self.msg = MIMEText(send_file, _subtype='html', _charset='utf-8')
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver
        # 添加附件
        # att = MIMEText(send_file,'plain','utf-8')
        # att["Content-Type"] = 'application/octet-stream'
        # att["Content-Disposition"] = 'attachment; filename="report.html"'
        # self.msg.attach(att)
        # self.msg['Subject'] = '自动化测试结果-----' + t
        self.msg['Subject'] = Header('Python自动化测试报告','utf-8')
        self.msg.attach(MIMEText('这是接口自动化报告邮件，如果想查看详情请查收附件', 'plain', 'utf-8'))
    # 发送邮件
    def send_email(self):
        self.config_mail()
        # 登录并发送邮件
        # try:
        # 实例化smtp对象
        smtp = smtplib.SMTP()
        # 链接smtp服务器
        smtp.connect(self.mail_host,self.mail_port)
        # 登录
        smtp.login(self.mail_user,self.mail_pass)
        # 发送邮件
        smtp.sendmail(self.sender,self.receiver,self.msg.as_string())
        print("邮件发送成功")
        # except smtplib.SMTPException as msg:
        #     print("邮件发送失败")

# if __name__ == '__main__':
s = sendEmail()
s.send_email()



