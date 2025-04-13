import unittest
from appium import webdriver
from find_element import BaseAction
import yaml
# from common.read_devices import app_device_cfg
# from page.my_page import MyCodeLoginPage,MyPwdLoginPage
import time


def app_device_cfg(device):
    with open('devices.yaml', 'r', encoding="utf-8")as file:
        data=yaml.load(file,Loader=yaml.FullLoader)
    for t in data:

        if device in t["desc"]:
            return t
        # print(t)

#读取手机配置参数
devices = ["设备9R", "设备_9黑色"]
a = []
for i in devices:
    cfg = app_device_cfg(device=i)
    # print(cfg)
    a.append(cfg)
print(a)
phone = ["15700000000","19911111111"]

class MyTestCase(unittest.TestCase):
    """
    快快登录测试
    """

    def setUp(self):
        """
        初始化相关环境
        :return:
        """
        #启动app
        element_1 = a.pop()
        self.driver = webdriver.Remote("http://127.0.0.1:%s/wd/hub" % element_1["port"], element_1["des"])
        self.driver = BaseAction(self.driver)
        self.phone = phone.pop()
        print(element_1)


    #
    def tearDown(self):
        print('结束')
        pass


    def test_login(self):
        """
        登录失败案例
        :return:
        """
        pass
    #     print('登录用例')
        # time.sleep(5)
        # self.element.find(MyCodeLoginPage.my).click()
        # self.element.find(MyCodeLoginPage.pwd_login).click()
        # time.sleep(5)
        # self.element.find(MyPwdLoginPage.phone).send_keys(self.phone)
        # self.element.find(MyPwdLoginPage.pwd).send_keys("123456")
        # self.element.find(MyPwdLoginPage.login_button).click()
        # #断言登录失败，还在登录页面
        # text = self.element.find(MyPwdLoginPage.forget_pwd).text
        # self.assertEqual(text,"忘记密码？")

# @ddt
# class Test_loging(unittest.TestCase):
#     def setUp(self):
#         # self.driver= init_driver()
#         self.login= Login_Page(self.driver)
#
#     @file_data('./data/login.yaml')
#     def test_01_longin(self,phone,password):
#         self.login.yewu_zuhe(phone,password)
#         # txt=self.login.get_login_info()
#         # print(txt)
#         # self.assertEqual(txt,result)
#
#     def tearDown(self):
#         sleep(2)
#         self.driver.quit()
#         # pass


if __name__ == '__main__':
    unittest.main()
