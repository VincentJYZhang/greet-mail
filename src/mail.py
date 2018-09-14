"""
    mail.py

    负责邮件的发送

    write on 2018.09.14
"""

__author__ = 'Vincent Zhang'

import usrconfig

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart,MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
import time
import os

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

class MailSender:

    @staticmethod
    def sendmail(receive_name, receive_mail, mess):

        from_addr = usrconfig.MAIL_USR
        password = usrconfig.MAIL_PWD
        to_addr = receive_mail
        smtp_server = usrconfig.MAIL_HOST

        msg = MIMEMultipart()
        msg.attach(MIMEText(mess, 'html', 'utf-8'))
        msg['From'] = _format_addr(usrconfig.myname + ' <' + from_addr + '>')
        msg['To'] = _format_addr(receive_name + ' <' + to_addr + '>')
        msg['Subject'] = Header('来自Vincent Zhang的问候', 'utf-8').encode()

        folder_path = usrconfig.FOLDER_PATH_
        if folder_path[-1] != '/':
            folder_path = folder_path + '/'

		# 格式化成2018-09-12形式
        time_str = time.strftime("%Y-%m-%d", time.localtime())

        img_name = folder_path + time_str + '.jpg'

        with open(img_name, 'rb') as f:

            mime = MIMEBase('image', 'jpg', filename='top.jpg')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='top.jpg')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)

        f.close()


        server = smtplib.SMTP(smtp_server, 25)
        # server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()



if __name__ == '__main__':
    mess = '<html><body><h1>Hello</h1>' + \
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' + \
    '</body></html>'

    MailSender.sendmail("张钧洋", "812400875@qq.com", mess)
