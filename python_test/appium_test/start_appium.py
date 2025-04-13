import os,time
import subprocess

def StartAppium(host="127.0.0.1",port=4723):
    """
    启动appium服务
    :param host: 访问地址
    :param port: 端口号
    :return:
    """
    a = os.popen('netstat -ano | findstr "%s" '% port)
    time.sleep(2)
    t1 = a.read()
    if "LISTENING" in t1:
        print("appium服务已经启动：%s" % t1)

    else:
        # 启动appium服务，指定bp端口号
        bootstrap_port = str(port + 1)
        # 把在cmd弹窗输入的命令，直接写到这里
        cmd = 'start /b appium -a %s -p %s -bp %s' % (host, port, bootstrap_port)
        # 去掉 “/b”，即可以打开cmd弹窗运行
        # cmd = 'start /b appium -a %s -p %s -bp %s' % (host, port, bootstrap_port)

        # 打印输入的cmd命令，及时间
        print("%s at %s " % (cmd, time.ctime()))

        subprocess.Popen(cmd, shell=True, stdout=open('./report' + str(port) + '.log', 'a'),
                         stderr=subprocess.STDOUT)

