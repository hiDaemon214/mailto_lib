#!/usr/bin/env python
#coding:utf-8
#新浪邮箱发送器

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
user,password = 'hidaemon@sina.com','7nTQLKG[KujxdBBG'
send_mail_title = '有新的档口发布'
recv_user = '1117205@qq.com'


def email(message):
    #构造MIMEText对象,第一个参数就是邮件正文,第二个参数是MIME的subtype
    # 传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
    msg = MIMEText(message, 'plain', 'utf-8')   #message为传入的参数,为发送的消息.
    """msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8') """
    #标准邮件需要三个头部信息： From, To, 和 Subject。
    msg['From'] = formataddr(["管理员",user])     #显示发件人信息
    msg['To'] = formataddr(["hidaemon",'1117205@qq.com'])          #显示收件人信息
    msg['Subject'] = send_mail_title     #定义邮件主题
    #zz123456@,.
    try:
        #创建SMTP对象
        server = smtplib.SMTP("smtp.sina.com", 25)
        #set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        #server.set_debuglevel(1)
        #login()方法用来登录SMTP服务器
        server.login(user,password)
        #sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
        server.sendmail(user, [recv_user,], msg.as_string())
        print u"邮件发送成功!"
        server.quit()
    except smtplib.SMTPException:
        print u"Error: 无法发送邮件"
if __name__ == '__main__':
    email("有新的档口发布了！")
    # cpu = 100
    # disk = 500
    # mem = 50
    # for i in range(1):
    #     if cpu > 90:
    #         alert = u"CPU出问题！"
    #         email(alert)
    #     if disk > 90:
    #         alert = u"硬盘出问题！"
    #         email(alert)
    #     if mem > 80:
    #         alert = u"内存出问题！"
    #         email(alert)
