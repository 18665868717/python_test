import smtplib  # python 对SMTP的支持，smtplib这个库负责发送邮件
from email.mime.text import MIMEText  # 发送邮件要填充的成员
from email.header import Header  # 设置编码方式
from BeautifulReport import BeautifulReport as BF
import time
import unittest
import os
import requests
def send_weixin_text():
    url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send"
    parem={"key":"fbe74359-cbc1-461c-a48a-afd209305850"}
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Content-Type": "application/json; charset=utf-8"
        }
    body=   {"msgtype": "text","text": {"content": "测试报告已生成，访问：http://120.25.172.129"}}
    requests.post(url=url,params=parem,headers=header,data=body)
# if __name__=='__main__':
#     report_name ='index.html'  # 组织测试报告的名称
#     current_path = os.getcwd()
#     obj=current_path+"/web_scripts/"
#     test_suite = unittest.defaultTestLoader.discover(obj,pattern='test_web*.py')  # 组织所有测试用例
#     runner = BF(test_suite)  # 类的实例化
import unittest
from BeautifulReport import BeautifulReport  # 导入BeautifulReport

if __name__ == '__main__':
    suite_tests = unittest.defaultTestLoader.discover("./web_scripts", pattern="test*.py",
                                                          top_level_dir=None)  # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    BeautifulReport(suite_tests).report(filename='index', description='car_web_test_测试集合',
                                            report_dir='./web_report/')  # log_path='.'把report放到当前目录下






    # path='/usr/share/nginx/html/'
    # runner.report(filename=report_name, report_dir=path,description='车贴接口测试')  # 使用类里的方法
    # # html_report = '../web_report/'+str(report_name) # 这个要注意要带目录路径，如果直接附文件名，程序会找不到路径
    # send_weixin_text() /Users/isentech/python_car_objact/web_scripts