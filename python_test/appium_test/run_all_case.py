from tomorrow import threads
# from common.start_appium import StartAppium
from test_login import MyTestCase
import unittest

#启动服务
# host = "127.0.0.1"
# for i in range(2):
#     port = 4723 + 2*i
#     StartAppium(host,port)
# #运行脚本，没有使用unittest框架
# devices = ["leidian","vivo"]
# pohe = ["15700000000","19911111111"]
# for i in range(len(devices)):
#     run_app(deviceName=devices[i],pohe=pohe[i])

#unittest用例
# pohe = ["15777936597","19960378307"]


@threads(2)    #添加线程
def run():
    """
    读取用例，运行脚本
    :return:
    """
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_login"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    #循环运行
    for i in range(2):
        print(i)
        run()
