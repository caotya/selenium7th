# 批量执行所有用例
import smtplib
import unittest

import os
from email.mime.text import MIMEText

from package.HTMLTestRunner import HTMLTestRunner
def send_emil(path):
    file = open(path,'rb')
    msg = file.read()
    mime=MIMEText( msg, _subtype='html', _charset="utf-8")
    mime['Subject'] = '博为峰自动化测试报告'
    mime['From'] = 'bwftest126@126.com'
    to = 'caotyi@126.com'
    mime['To'] = to

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login('bwftest126@126.com', 'abc123asd654')
    smtp.send_message(mime,form_addr='bwftest126@126.com',to_addrs=to, msg=mime.as_string())
    smtp.quit()

if __name__ == '__main__':
    # 只能执行继承了unittest.testCase的类
    suit = unittest.defaultTestLoader.discover('./Day5', pattern='*Test.py')
    # unittest.TextTestRunner().run(suit)
    base_path = os.path.dirname(__file__)
    path = base_path+'/report/test_report.html'
    file = open(path,'wb')


    HTMLTestRunner(stream=file, verbosity=1, title="博为峰测试报告", description="阿拉啦啦啦经济技术计算机呜呜呜呜呜").run(suit)
