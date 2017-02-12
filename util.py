# coding=utf8

import smtplib
import httplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


def assertEqual(a, b):
    if a == b:
        return True
    else:
        return False

def fetch(hostname, path):
    httpClient = None
    httpClient = httplib.HTTPConnection(hostname, 80, timeout=30)
    httpClient.request('GET', path)
    return httpClient.getresponse()

def reportEmail(content):
    sender = 'yanhaijingtest@sohu.com'
    receivers = 'wsluyu2011@163.com'
    password = '776771343'

    msg=MIMEMultipart()
    msg['From']=sender
    msg['To']=receivers
    msg['Subject']='[monitor] monitor error!!!'

    con=MIMEText(content, 'html')
    msg.attach(con)
    try:
        smtpObj = smtplib.SMTP('smtp.sohu.com')
        smtpObj.set_debuglevel(1)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(sender, password)

        smtpObj.sendmail(sender, receivers, msg.as_string())
        smtpObj.quit()
        print "send email: success"
    except smtplib.SMTPException:
        print "send email: failed"

def reportFile(content):
    print 'write file:'
    output = open('temp.txt', 'a')
    output.write(content + '\n')
    output.close()
