#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: email_utils.py
# @time: 2020/5/10 9:57 上午

import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailUtils:
    def __init__(self, smtp_subject, smtp_body, smtp_file_path=None):
        self.smtp_server = 'smtp.qq.com'
        self.smtp_sender = '329999897@qq.com'
        self.smtp_senderpassword = 'wvcsgattkyqqbhah'  # 479262985@qq.com
        self.smtp_receiver = '329999897@qq.com'  # 'newdream1@qq.com,newdream2@qq.com,newdream3@qq.com'
        self.smtp_cc = ''  # 'newdream4@qq.com,newdream5@qq.com'
        self.smtp_subject = smtp_subject
        self.smtp_body = smtp_body
        self.smtp_file = smtp_file_path

    def mail_content(self):
        if self.smtp_file != None:
            msg = MIMEMultipart()
            with open(self.smtp_file, 'rb') as f:
                mime = MIMEBase('zip', 'zip', filename=self.smtp_file.split('/')[-1])
                mime.add_header('Content-Disposition', 'attachment',
                                filename=('gb2312', '', self.smtp_file.split('/')[-1]))
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                msg.attach(mime)
            msg.attach(MIMEText(self.smtp_body, "html", "utf-8"))
            msg['from'] = self.smtp_sender
            msg['to'] = self.smtp_receiver  # ",".join(self.smtp_receiver)
            msg['Cc'] = self.smtp_cc  # ",".join(self.smtp_cc)
            msg['subject'] = self.smtp_subject
            return msg
        else:
            msg = MIMEText(self.smtp_body, "html", "utf-8")
            msg['from'] = self.smtp_sender
            msg['to'] = self.smtp_receiver
            msg['Cc'] = self.smtp_cc
            msg['subject'] = self.smtp_subject
            return msg

    def send_mail(self):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        except:
            smtp = smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        mail_content = self.mail_content()
        try:
            smtp.sendmail(self.smtp_sender, self.smtp_receiver.split(',') + self.smtp_cc.split(','),
                          mail_content.as_string())
        except Exception as e:
            print('发送失败')
        smtp.quit()
