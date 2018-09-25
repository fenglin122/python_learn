#!/usr/bin/env python
# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib


def send_html_email(content, receiver, subject):
    password = 'Qq393912540'
    sender = 'wangyqa@litsoft.com.cn'
    # receiver = 'wangyq35@lenovo.com'
    # subject = '数据监控推送'
    stmpserver = 'smtp.exmail.qq.com'
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    stmp = smtplib.SMTP()
    stmp.connect(stmpserver)
    stmp.login(sender, password)
    stmp.sendmail(sender, receiver, msg.as_string())
    stmp.quit()


def send_mime_email(content, receiver, subject, file_path, file_name, cc=[]):
    password = 'Qq393912540'
    sender = 'wangyqa@litsoft.com.cn'
    # receiver = 'wangyq35@lenovo.com'
    # subject = '数据监控推送'
    stmpserver = 'smtp.exmail.qq.com'
    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['to'] = ','.join(receiver)
    msg['Cc'] = ','.join(cc)
    msg.attach(MIMEText(content, 'plain', 'utf-8'))
    file_paths = file_path.split(",")
    file_names = file_name.split(",")
    for i, file_path in enumerate(file_paths):
        attr = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
        attr['Content-Type'] = 'appliction/octet-stream'
        attr.add_header("Content-Disposition", "attchment", filename=("utf-8", "", file_names[i]))
        msg.attach(attr)
    # 非中文名写法
    # attr['Content-Disposition'] = 'attchment; filename=2018-03-28pvuv.xls'

    stmp = smtplib.SMTP()
    stmp.connect(stmpserver)
    stmp.login(sender, password)
    stmp.sendmail(sender, receiver+cc, msg.as_string())
    stmp.quit()


if __name__ == '__main__':
    content = '测试正文'
    receiver = ['wangyq35@lenovo.com']
    subject = '测试收件人显示和抄送人显示'
    file_path = 'get_config_from_json.py'
    file_name = '测试附件'
    cc = []
    send_mime_email(content, receiver, subject, file_path, file_name, cc)
