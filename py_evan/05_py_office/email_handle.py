# coding:utf-8
# time: 2023/5/14
# author: evan
# python操作email

import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import schedule


class EmailHandler:
    mail_host = 'smtp.qq.com'
    mail_user = '2696612575@qq.com'
    mail_password = 'ihvtuvwhuzxpdedf'
    receiver = ['ldk2696612575@gmail.com']

    def send(self):
        message = MIMEText('test msg', 'plain', 'utf-8')
        message['From'] = Header(self.mail_user)
        message['Subject'] = Header('python脚本测试', 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)
            smtpObj.login(self.mail_user, self.mail_password)
            smtpObj.sendmail(self.mail_user, self.receiver, message.as_string())
        except smtplib.SMTPException as e:
            print(e)

    def send_html(self):
        message = MIMEText('<p color:"red";>test msg</p>', 'html', 'utf-8')
        message['From'] = Header(self.mail_user)
        message['Subject'] = Header('python脚本测试', 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)
            smtpObj.login(self.mail_user, self.mail_password)
            smtpObj.sendmail(self.mail_user, self.receiver, message.as_string())
        except smtplib.SMTPException as e:
            print(e)

    def send_with_multipart(self):
        """
        带附件的邮件发送
        :return:
        """
        print('send_start')
        message = MIMEMultipart()
        message['From'] = Header(self.mail_user)
        message['Subject'] = Header('python脚本测试A', 'utf-8')

        attr = MIMEText(open('email_handle.py', 'rb').read(), 'base64', 'utf-8')
        attr['Content-Type'] = 'application/octet-stream'
        attr['Content-Disposition'] = 'attachment;filename="email_handle.py"'
        message.attach(attr)
        message.attach(MIMEText('这是一个带附件的邮件', 'plain', 'utf-8'))

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)
            smtpObj.login(self.mail_user, self.mail_password)
            smtpObj.sendmail(self.mail_user, self.receiver, message.as_string())
        except smtplib.SMTPException as e:
            print(e)


if __name__ == '__main__':
    email = EmailHandler()
    # email.send_html()

    # 定时任务
    schedule.every(30).seconds.do(email.send_with_multipart)
    while True:
        schedule.run_pending()
        time.sleep(1)
