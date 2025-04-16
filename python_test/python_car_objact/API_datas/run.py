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
if __name__=='__main__':
    os.system("rm -rf/usr/share/nginx/html/* ")
    # ctime = time.strftime('%Y-%m-%d_%H-%M-%S')  # 获取当前时间
    report_name ='index.html'  # 组织测试报告的名称
    Path=os.path.dirname(os.getcwd())#获取上一级目录名字
    case_test=Path+"/API_test/"
    test_suite = unittest.defaultTestLoader.discover(case_test,pattern='test_*.py')  # 组织所有测试用例
    runner = BF(test_suite)  # 类的实例化
    path='/usr/share/nginx/html/'
    runner.report(filename=report_name, report_dir=path,description='车贴接口测试')  # 使用类里的方法
    # html_report = '../web_report/'+str(report_name) # 这个要注意要带目录路径，如果直接附文件名，程序会找不到路径
    send_weixin_text()


    # sender = "lizepeng6578712@qq.com"
    # pwd = "mdbbhjqdmgilbjaf"  # 发送方邮箱sender的授权码,
    # receivers = "354244541@qq.com"
    # f = open(html_report,'rb')
    # content=f.read()
    # f.close()
    # message = MIMEText(content, 'html', 'utf-8')  # 发送含HTML内容的邮件
    # message['To'] = receivers  # 填入收件人邮箱地址，用Header('聊天记录','utf-8')这个是绝对不行的，邮箱收和发的人的邮箱地址不用设置编码方式
    # message['From'] = sender  # 填入发件人邮箱地址，用Header('yj 和 DH','utf-8') 这个是绝对不行的，邮箱收和发的人的邮箱地址不用设置编码方式
    # # subject = 'Python SMTP 最新 邮件测试' + ' 发送时间： '+ str_time
    # subject = 'Python SMTP Car接口测试' + ' 发送时间： ' + ctime
    # # message['Subject'] = subject #可以不设置编码
    # message['Subject'] = Header(subject, 'utf-8')
    # try:
    #     smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465) #邮箱服务地址和端口
    #     smtpObj.login(sender, pwd)  # 登录认证
    #     smtpObj.sendmail(sender, receivers, message.as_string(),)  # 发送邮件主题
    #     print('邮件发送成功！')
    # except smtplib.SMTPException as e:
    #     print('邮件发送失败，失败原因：', e)




    # import smtplib
    # from email.mime.text import MIMEText
    # from email.mime.multipart import MIMEMultipart
    # from email.mime.application import MIMEApplication
    #
    # # 邮件内容
    # msg = MIMEMultipart()
    # msg['Subject'] = 'python_cat_test:'+ report_name
    # msg['From'] = "lizepeng6578712@qq.com"
    # msg['To'] = "354244541@qq.com"
    #
    # # 添加文本内容
    # text = MIMEText('车贴接口测试报告，需要下载附件保存至本地后在本地打开，才能完整查看内容')
    # msg.attach(text)
    #
    # # 添加附件
    # with open(html_report, 'rb') as f:
    #     attachment = MIMEApplication(f.read())
    #     attachment.add_header('Content-Disposition', 'attachment', filename='Car_Test_Api_Report'+".html")
    #     msg.attach(attachment)
    #
    # # 发送邮件
    # smtp_server = 'smtp.qq.com'
    # smtp_port = 25
    # smtp_user = "lizepeng6578712@qq.com"
    # smtp_password = "mdbbhjqdmgilbjaf"
    # server = smtplib.SMTP(smtp_server, smtp_port)
    # server.login(smtp_user, smtp_password)
    # server.sendmail(msg['From'], msg['To'], msg.as_string())
    # server.quit()


