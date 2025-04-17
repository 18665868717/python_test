import sys
from telnetlib import EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from web_beas import base_action
from ddt import file_data,ddt
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from selenium.webdriver.support import expected_conditions as EC

@ddt()
class Test_loging(unittest.TestCase):

    # def __int__(self):
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # driver = webdriver.Chrome(options=chrome_options)


    def setUp(self):
        self.driver= webdriver.Chrome('/usr/local/chromedriver.exe')
        self.driver.get('https://tuying.mncats365.com/web/index.html#/login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        sleep(1)

        # self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        # self.chrome_options.add_argument('--disable-gpu')
        # self.chrome_options.add_argument("--window-size=2560,1440")
        # self.driver = webdriver.Chrome(options=self.chrome_options)
        # self.driver.get('https://tuying.mncats365.com/web/index.html#/login')
        # sleep(1)
        # self.driver.implicitly_wait(30)

    def login_methon(self):
        self.driver.find_element('xpath', '//*[@id="app"]/div/div[2]/div[1]/div[2]').click()
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div>div>div>div>input").clear()
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div>div>div>div>input").send_keys(18665868717)
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div:nth-child(2)>div>div>div>input").clear()
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div:nth-child(2)>div>div>div>input").send_keys(111111)
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div:nth-child(4)").click()

    @file_data("../web_datas/login_datas/login_data.yaml")
    def test_0001_login(self,username,password,result,):
        """登录"""
        self.driver.find_element('xpath','//*[@id="app"]/div/div[2]/div[1]/div[2]').click()
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div>div>div>div>input").clear()
        self.driver.find_element(By.CSS_SELECTOR,"form#login>div>div>div>div>input").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div:nth-child(2)>div>div>div>input").clear()
        self.driver.find_element(By.CSS_SELECTOR,"form#login>div:nth-child(2)>div>div>div>input").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,"form#login>div:nth-child(4)").click()
        sleep(1)
        toast = self.driver.find_element(By.XPATH,'/html/body/div[2]/p').text
        # text = toast.get_attribute('textContent')
        # # if text == "登录成功":
        # #     cookie = self.driver.get_cookies()
        # #     print(cookie)
        self.assertEqual(toast,result)

    def test_0002_xq_cz(self):
        """获取警报表单内容"""
        data=[]
        self.driver.find_element('xpath', '//*[@id="app"]/div/div[2]/div[1]/div[2]').click()
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div>div>div>div>input").clear()
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div>div>div>div>input").send_keys(18665868717)
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div:nth-child(2)>div>div>div>input").clear()
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div:nth-child(2)>div>div>div>input").send_keys(111111)
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div:nth-child(4)").click()
        table =self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[3]/div[1]/div[2]/table')  #表单元素
        # 获取表格所有
        ooo=table.find_elements(By.TAG_NAME,"tr")
        for i in ooo:
            data.append(i.text)
        print(data)


    def test_0003_all_device_status(self):
        """获取名下设备状态"""
        self.driver.find_element('xpath', '//*[@id="app"]/div/div[2]/div[1]/div[2]').click()
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div>div>div>div>input").clear()
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div>div>div>div>input").send_keys(18665868717)
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div:nth-child(2)>div>div>div>input").clear()
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div:nth-child(2)>div>div>div>input").send_keys(111111)
        self.driver.find_element(By.CSS_SELECTOR, "form#login>div:nth-child(4)").click()
        device_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div[1]/div[1]').text #全部设备（1）
        on_line=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div[1]/div[3]/p[1]').text #在线设备
        on_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div[1]/div[3]/p[2]').text#1
        off_lien=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div[1]/div[4]/p[1]').text
        off_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div[1]/div[4]/p[2]').text
        on_line_num=on_line+on_num
        off_lien_num=off_lien+off_num
        self.assertEqual(device_num,"全部设备（1）")
        self.assertEqual(on_line_num,"在线设备1")
        self.assertEqual(off_lien_num,"离线设备0")
        print("名下设备数量：{},其中{}、{}。".format(device_num,on_line_num,off_lien_num))

    def test_0004_on_lien_devive_status(self):
        """在线设备的状态"""
        self.login_methon()
        move_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div[2]/div[3]/p[2]').text
        stationary_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div[2]/div[4]/p[2]').text
        standby_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div[2]/div[5]/p[2]').text
        if move_num=='1' and stationary_num=='0' and standby_num=='0':
            device_status=True
        elif move_num=='0' and stationary_num=='1' and standby_num=='0':
            device_status = True
        elif move_num == '0' and stationary_num == '0' and standby_num == '1':
            device_status = True
        else:
            device_status= False
        self.assertTrue(device_status,True)
        print("当前在线设备状态，运动{}，静止{}，待机{}.那么下个用例离线判断条件为0为通过".format(move_num,stationary_num,standby_num))

    def test_0005_off_device_status(self):
        """离线设备的状态"""
        self.login_methon()
        expired_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div[3]/div[3]/p[2]').text
        off_line_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div[3]/div[4]/p[2]').text
        shutdown_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div[3]/div[5]/p[2]').text
        if expired_num=='0' and off_line_num=='0' and shutdown_num=='0':
            device_status=True
        else:
            device_status= False
        self.assertTrue(device_status,True)
        print("当前离线设备状态：过期{}、离线{}、关机{}".format(expired_num,off_line_num,shutdown_num))

    def test_0006_today_alert(self):
        """今日警报"""
        self.login_methon()
        title_today_alert=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[3]/div[2]/div[1]').text
        move_alert=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[3]/div[2]/div[4]/div[1]/p[1]').text
        move_alert_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[3]/div[2]/div[4]/div[1]/p[2]').text
        emoval_alert=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[3]/div[2]/div[4]/div[2]/p[1]').text
        emoval_alert_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[3]/div[2]/div[4]/div[2]/p[2]').text
        fence_alert=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[3]/div[2]/div[4]/div[3]/p[1]').text
        fence_alert_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[3]/div[2]/div[4]/div[3]/p[2]').text
        low_battery=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[3]/div[2]/div[4]/div[4]/p[1]').text
        low_battery_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[3]/div[2]/div[4]/div[4]/p[2]').text
        in_fence_shutdown=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[3]/div[2]/div[4]/div[5]/p[1]').text
        in_fence_shutdown_num=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[3]/div[2]/div[4]/div[5]/p[2]').text
        move_status=move_alert+move_alert_num
        emoval_status=emoval_alert+emoval_alert_num
        fence_status=fence_alert+fence_alert_num
        low_battery_status=low_battery+low_battery_num
        in_fence_shutdown_status=in_fence_shutdown+in_fence_shutdown_num
        print("今日警报标题：{},{}、{}、{}、{}、{}".format(title_today_alert,move_status,emoval_status,fence_status,low_battery_status,in_fence_shutdown_status))

    def test_0007_console(self):
        """控制中心，状态过滤"""
        self.login_methon()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/ul/li[2]').click()
        device_all=self.driver.find_element(By.XPATH,'//*[@class="el-input__wrapper"]/input').text
        on_line_device=self.driver.find_element(By.XPATH,'//*[@class="el-button el-button--info online"]/span').text
        off_line_device=self.driver.find_element(By.XPATH,'//*[@class="el-button el-button--info offline"]/span').text
        print("控制中心，所有设备:{},{},{}".format(device_all, on_line_device, off_line_device))
        #选择运动
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span/span').click()
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div[1]/ul/li[2]').click()
        status_remove= self.driver.find_element(By.XPATH, '//*[@class="el-input__wrapper"]/input').text
        # print(status_remove)
        sleep(1)

        # 选择静止
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span/span').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/ul/li[3]').click()
        status_still = self.driver.find_element(By.XPATH, '//*[@class="el-input__wrapper"]/input').text
        sleep(1)

        # 选择待机
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span/span').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/ul/li[4]').click()
        status_standby = self.driver.find_element(By.XPATH, '//*[@class="el-input__wrapper"]/input').text
        sleep(1)

        # 选择离线
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span/span').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/ul/li[5]').click()
        status_offline = self.driver.find_element(By.XPATH, '//*[@class="el-input__wrapper"]/input').text
        sleep(1)

        # 选择关机
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span/span').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/ul/li[6]').click()
        sleep(1)

        status_shutdown = self.driver.find_element(By.XPATH, '//*[@class="el-input__wrapper"]/input').text

        # 选择过期
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span/span').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/ul/li[7]').click()
        status_exceed = self.driver.find_element(By.XPATH, '//*[@class="el-input__wrapper"]/input').text
        sleep(1)

        print("控制中心，所有设备{},在线设备{},离线设备{}".format(device_all,on_line_device,off_line_device))
        print("选择运动状态后:点击的是{},选择禁止状态后:点击的是{},选择待机状态后:点击的是{},选择离线状态后:点击的是{},选择关机状态后:点击的是{},选择过期状态后:点击的是{},"
              .format(status_remove,status_still,status_standby,status_offline,status_shutdown,status_exceed))

    @file_data('../web_datas/login_datas/console_search.yaml')
    def test_0008_console_search(self,content,result):
        """控制中心，搜索设备"""
        self.login_methon()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/ul/li[2]').click()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div/input').send_keys(content)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div/div[1]/div[2]/button').click()
        try:
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div/div')
            rep = True
            self.assertEqual(rep, result)

        except NoSuchElementException as e:
            print(e)
            rep= True
            self.assertEqual(rep, result)

    def test_0009_console_location(self):
        """控制中心，查看位置"""
        self.login_methon()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/ul/li[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div/div').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="devicePopup"]/div[8]/div[1]').click()
        toast_txt=self.driver.find_element(By.XPATH,'/html/body/div[3]/p').text
        print(toast_txt)
        self.assertIsNotNone(toast_txt)

    def test_0010_console_setting(self):
        """控制中心，设置"""
        self.login_methon()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/ul/li[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div/div').click()
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="devicePopup"]/div[8]/div[2]').click()
        sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[4]/div/div/div/div/div[8]/button[2]').click()
        toast_txt=self.driver.find_element(By.XPATH,'/html/body/div[3]/p').text
        print("调试信息",toast_txt)
        self.assertEqual(toast_txt,'配置成功')

    def test_0015_console_enewal(self):
        """控制中心，设备续期"""
        self.login_methon()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/ul/li[2]').click()  #控制中心
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div/div').click()#设备
        sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div[8]/div[3]').click()
        device_name=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[5]/div/div/div/div/div[1]/span[1]').text
        device_number=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[5]/div/div/div/div/div[1]/span[2]').text
        device_time=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[5]/div/div/div/div/div[2]').text
        device_enewal_title=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[5]/div/div/div/div/div[3]/div/span').text
        price_1=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[5]/div/div/div/div/div[3]/div/div/label[1]/span[2]').text
        price_2=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[5]/div/div/div/div/div[3]/div/div/label[2]/span[2]').text
        price_3=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[5]/div/div/div/div/div[3]/div/div/label[3]/span[2]').text
        price_4=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[5]/div/div/div/div/div[3]/div/div/label[4]/span[2]').text
        print("服务续期信息：{}\t{}\n{}\n{}\t{}\t{}\t{}\t{}".format(device_name,device_number,device_time,device_enewal_title,price_1,price_2,price_3,price_4))

    def test_0020_console_remote(self):
        """控制中心，远程待机"""
        self.login_methon()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/ul/li[2]').click()  #控制中心
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div/div').click()#设备
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div[8]/div[4]').click()#远程控制
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[2]/div[6]/div/div/div/div/div[3]/div/label[2]/span[1]').click()#点击待机
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[2]/div[6]/div/div/div/div/div[5]/button[2]').click()#点击确定
        toast_txt=self.driver.find_element(By.XPATH, '/html/body/div[3]/p').text
        print(toast_txt)
        self.assertEqual(toast_txt,"设备已待机")

    def test_0021_console_rouse(self):
        """控制中心，远程唤醒"""
        self.login_methon()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/ul/li[2]').click()  # 控制中心
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div/div').click()  # 设备
        sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div[8]/div[4]').click()  # 远程控制
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[6]/div/div/div/div/div[3]/div/label[1]/span[1]').click() #勾选唤醒
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[6]/div/div/div/div/div[5]/button[2]').click() #点击确定
        toast_txt=self.driver.find_element(By.XPATH,'/html/body/div[3]/p').text
        print(toast_txt)
        self.assertEqual(toast_txt,"设备已唤醒")

    @unittest.skip
    def test_0022_console_showdown(self):
        """关机操作不处理"""
        self.login_methon()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/ul/li[2]').click()  # 控制中心
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/div/div').click()  # 设备
        sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div[8]/div[4]').click()  # 远程控制
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[6]/div/div/div/div/div[3]/div/label[3]/span[1]').click()  # 勾选唤醒
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[2]/div[6]/div/div/div/div/div[5]/button[2]').click()  # 点击确定
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]').click()  # 点击确定

        toast_txt = self.driver.find_element(By.XPATH, '/html/body/div[3]/p').text
        print(toast_txt)
        self.assertEqual(toast_txt, "设备已关机")
        self.test_0021_console_rouse()
    #
    # def test_0030_track_data(self):
    # """时间不太好处理"""
    #     self.login_methon()
    #     self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[3]').click()#
    #     self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[2]/form/div[2]/div/div/div').click()#点击下拉框
    #     # start_time=self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div[1]/ul/li[1]')#选择今天
    #     self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div[1]/ul/li[1]').click()#选择今天
    #     # start_time=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[2]/form/div[3]/div/div[1]/div')

    @file_data('../web_datas/login_datas/fence_data.yaml')
    def test_0050_fence_manage(self,radius,setting,fence_name,result):
        """围栏管理，添加围栏"""
        self.login_methon()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/ul/li[4]').click() #点击围栏管理
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/div[1]/button').click() #点击添加围栏

        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div/div/div/input').clear()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div[1]/div/input').send_keys(radius)#围栏半径
        if setting==1:
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[3]/div/div/label[1]/span[1]').click() #勾选进
            # self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[4]/div/span/span/span').click()
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[5]/div/div/div/div[2]/div/input').click()#点击选择设备栏
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/ul/li').click()#点击设备
            # self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div/div/div/input').click()#点击位置输入
            # self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[6]/div/div/div/input').click()
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[6]/div/div/div/input').send_keys(fence_name)#输入围栏名称
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/button[2]').click()
            toast_txt = self.driver.find_element(By.XPATH, '/html/body/div[3]/p').text

            self.assertEqual(toast_txt, result)
        elif setting==2:

            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[3]/div/div/label[2]/span[1]').click()
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[4]/div/div/div/div[2]/div/input').click()
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/ul/li').click()
            sleep(1)
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div/div/div/input').click()
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[5]/div/div/div/input').send_keys(fence_name)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/button[2]').click()
            sleep(1)
            toast_txt = self.driver.find_element(By.XPATH, '/html/body/div[3]/p').text

            self.assertEqual(toast_txt, result)

        elif setting==3:
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[3]/div/div/label[1]/span[1]').click()
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[3]/div/div/label[2]/span[1]').click()
            # self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[4]/div/span/span/span').click()
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[5]/div/div/div/div[2]/div/input').click()
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/ul/li').click()
            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div/div/div/input').click()
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[6]/div/div/div/input').send_keys(fence_name)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/button[2]').click()
            toast_txt = self.driver.find_element(By.XPATH, '/html/body/div[3]/p').text
            self.assertEqual(toast_txt, result)

    def test_0051_fence_add_number(self):
        """获取添加围栏的数量，判断和上一个用例添加的是否一致"""
        self.login_methon()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[4]').click() #点击围栏管理
        ele_list=self.driver.find_elements(By.XPATH,'//*[@class="footerItem"]')#获取围栏数量
        sum=int(len(ele_list))
        self.assertEqual(sum,4)

    def test_0052_fence_del_single(self):
        """删除单个围栏"""
        self.login_methon()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[4]').click()#点击围栏管理
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/div/label/span').click()#勾选第一个设备
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/div[1]/div/i').click()#点击删除
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]').click()#点击删除后的确定按钮
        sleep(1)
        ele_list=self.driver.find_elements(By.XPATH,'//*[@class="footerItem"]')#获取围栏数量
        sum=int(len(ele_list))
        self.assertEqual(sum,3)

    def test_0053_fence_edit_status(self):
        """修改围栏启用状态"""
        self.login_methon()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[4]').click()#点击围栏管理
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div[2]/div/span[1]').click()
        element=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div[2]/div/span[2]/span')
        aria_hidden=element.get_attribute('aria-hidden')
        toast_txt=self.driver.find_element(By.XPATH,'/html/body/div[3]/p').text
        print(aria_hidden,toast_txt)
        self.assertEqual(aria_hidden,'true')
        self.assertEqual(toast_txt,'状态更改成功')

    def test_0054_fence_del_all(self):
        """删除所有围栏"""
        self.login_methon()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[4]').click()#点击围栏管理
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/div[1]/div/label/span[1]').click()#点击全选
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div[1]/div[1]/div/i').click()#点击删除
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]').click()#点击删除后的确定按钮
        sleep(1)
        ele_list=self.driver.find_elements(By.XPATH,'//*[@class="footerItem"]')#获取围栏数量
        sum=int(len(ele_list))
        self.assertEqual(sum,0)
    #
    # """编辑围栏先留着还没有写"""
    #
    def test_0060_device_mange_del(self):
        """设备管理删除设备"""
        self.login_methon()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[5]').click()#点击设备管理
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/label').click()#勾选第一个设备
        self.driver.find_element(By.XPATH,'//html/body/div[1]/div/div[3]/div/div[1]/button[2]').click()#点击删除
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]').click()#点击删除后的确定按钮
        toast_txt=self.driver.find_element(By.XPATH,'/html/body/div[3]/p').text#获取toast提示的文本
        self.assertEqual(toast_txt,'删除设备成功')

    def test_0061_device_mange_del_null(self):
        """不选择设备进行删除"""
        self.login_methon()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[5]').click()#点击设备管理
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/button[2]').click()#点击顶部删除
        toast_txt=self.driver.find_element(By.XPATH,'/html/body/div[3]/p').text#获取toast提示的文本
        self.assertEqual(toast_txt,'请选择要删除的设备')

    @file_data('../web_datas/login_datas/add_device_data.yaml')
    def test_0062_device_mange_add(self,device_number,device_name,status,result):
        """添加设备"""
        self.login_methon()
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[5]').click()  # 点击设备管理
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/button[1]').click()  # 点击添加设备
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div/form/div[1]/div/div/div/input').send_keys(device_number)  # 输入设备编号
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div/form/div[2]/div/div/div/input').send_keys(device_name)  # 输入设备名称
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div/form/div[3]/div/button').click() # 添加设备的添加按钮

        if status==1:
            sleep(1)
            toast_info=self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div/form/div[1]/div/div[2]').text#获取编号输入错误提示的信息
            self.assertEqual(toast_info,result)
        elif status==2:
            sleep(1)
            toast_info=self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div/form/div[2]/div/div[2]').text#
            self.assertEqual(toast_info,result)
        else:
            sleep(1)
            toast_info = self.driver.find_element(By.XPATH,'/html/body/div[3]/p').text  #
            self.assertEqual(toast_info,result)

    def test_0063_device_mange_getlistinfo(self):
        """获取整个设备列表信息"""
        self.login_methon()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[5]').click()  # 点击设备管理
        device_list=self.driver.find_element(By.XPATH, '//html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table')  # 点击设备管理
        # conteng=len(device_list.find_elements(By.TAG_NAME,'td'))
        content=len(device_list.find_elements(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr'))
        self.assertEqual(content,1)
        print("当前只有一个设备，获取设备列表数量是{}".format(content))
        # for i in conteng:
        #     print(i.text)
    def test_0064_device_mange_edit_device_info(self):
        """编辑设备详情信息"""
        self.login_methon()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[5]').click()  # 点击设备管理
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[7]/div/span[1]').click()  #
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[8]/button[1]').click()  # 编辑信息

        form_ele=self.driver.find_element(By.TAG_NAME,'form')
        form_ele.find_element(By.XPATH,'div[3]/div/div/div/input').send_keys("楚：好几个8")
        form_ele.find_element(By.XPATH,'div[4]/div/div/div/input').send_keys("五颜六色")
        form_ele.find_element(By.XPATH,'div[5]/div/div/textarea').send_keys("测试设备备注信息")
        form_ele.find_element(By.XPATH,'div[6]/div/div/button[2]').click()

        toast_info=self.driver.find_element(By.XPATH,'/html/body/div[3]/p').text
        self.assertEqual(toast_info,"修改成功")

    def test_0065_device_mange_details(self):
        """查看设备详情信息"""
        self.login_methon()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[5]').click()  # 点击设备管理
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[7]/div/span[1]').click()  #
        sleep(1)
        device_name=self.driver.find_element(By.CSS_SELECTOR, '#app>div>div.content>div>div.device_info>div.device_left>div.device_name>span').text  # 点击详情
        device_type = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[2]').text
        device_number = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[3]').text
        car_number = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[5]').text
        car_colour = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[6]').text
        note_info = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[7]').text
        print("{}\n{}\n{}\n{}\n{}\n{}".format(device_name,device_type,device_number,car_number,car_colour,note_info))
        self.assertEqual(car_number,"车牌号:楚：好几个8")
        self.assertEqual(car_colour,"车辆颜色:五颜六色")
        self.assertEqual(note_info,"备注:测试设备备注信息")

    def test_0066_device_mange_details_alert(self):
        """查看设备详情信息"""
        alert_list=[]
        self.login_methon()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[5]').click()  # 点击设备管理
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[7]/div/span[1]').click()  #
        sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[2]').click()#点击警报
        eles=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div[3]/div[2]/div[1]/div[3]/div/div[1]/div/table')
        row=eles.find_elements(By.TAG_NAME,'tr')
        for i in row:
            alert_list.append(i.text)
        print(alert_list)
        # print(len(row))
        self.assertIsNotNone(alert_list)
    """设备管理-详情-围栏管理没写"""
    def test_0070_device_mange_renew(self):
        """设备管理，获取设备续期信息"""
        self.login_methon()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[5]').click()  # 点击设备管理
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[7]/div/span[2]').click()  # 续期
        device_name=self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[5]/div/div/div/div/div[1]/span[1]').text  # 续期
        device_number=self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[5]/div/div/div/div/div[1]/span[2]').text  # 续期
        device_time=self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[5]/div/div/div/div/div[2]').text  # 续期
        device_mon=self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[5]/div/div/div/div/div[3]/div/div').text  # 续期
        print("续期的文本显示内容如下：\n{}\n{}\n{}\n{}".format(device_name,device_number,device_time,device_mon))
    #
    def test_0071_device_mange_cat_loction(self):
        """设备管理，查看位置"""
        self.login_methon()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[5]').click()  # 点击设备管理
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[7]/div/span[5]').click()  # 点击查看位置
        try:
            ele=self.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div')

        except :
            self.assertTrue(False)

    def test_0072_alert_mange_all(self):
        """查看所有警报"""
        self.login_methon()
        datas=[]
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[6]').click()
        ele=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody')
        ele_tr=ele.find_elements(By.TAG_NAME,'tr')
        for i in ele_tr:
            datas.append(i.text)
        print(datas)

    def test_0073_alert_mange_today(self):
        """查看今日警报"""
        self.login_methon()
        datas=[]
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[6]').click()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[1]/button[1]').click()
        sleep(1)
        ele=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody')
        # ele=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody')
        ele_tr=ele.find_elements(By.TAG_NAME,'tr')
        for i in ele_tr:
            datas.append(i.text)
        print(datas)

    def test_0074_alert_mange_setting_remove(self):
        """设置是否开启运动警报状态"""
        self.login_methon()
        sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[6]').click()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[2]/button').click()#点击警报设置
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[1]/div[2]/span[1]/div').click()#点击修改状态
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[1]/div[2]/span[1]/div').click()#点击修改状态
        sleep(1)
        toast_txt=self.driver.find_element(By.XPATH,'/html/body/div[4]/p').text
        self.assertEqual(toast_txt,'修改成功')
    #
    def test_0075_alert_mange_setting_dismantled(self):
        self.login_methon()
        sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[6]').click()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[2]/button').click()#点击警报设置
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[1]/div[2]/span[2]/div').click()#点击修改状态
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[1]/div[2]/span[2]/div').click()#点击修改状态
        sleep(1)
        toast_txt=self.driver.find_element(By.XPATH,'/html/body/div[4]/p').text
        self.assertEqual(toast_txt,'修改成功')
    #
    def test_0075_alert_mange_setting_lowpowe(self):
        self.login_methon()
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[6]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/button').click()  # 点击警报设置
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[1]/div[2]/span[3]/div').click()  # 点击修改状态
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[1]/div[2]/span[3]/div').click()  # 点击修改状态
        toast_txt = self.driver.find_element(By.XPATH, '/html/body/div[4]/p').text
        self.assertEqual(toast_txt, '修改成功')
    #
    def test_0076_alert_mange_setting_fence(self):
        self.login_methon()
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[6]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/button').click()  # 点击警报设置
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[1]/div[2]/span[4]/div').click()  # 点击修改状态
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[1]/div[2]/span[4]/div').click()  # 点击修改状态
        toast_txt = self.driver.find_element(By.XPATH, '/html/body/div[4]/p').text
        self.assertEqual(toast_txt, '修改成功')
    #
    def test_0077_alert_mange_setting_tent(self):
        self.login_methon()
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[6]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/button').click()  # 点击警报设置
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[2]/div[2]/span[4]/div').click()  # 点击修改状态
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[2]/div[2]/span[4]/div').click()  # 点击修改状态
        toast_txt = self.driver.find_element(By.XPATH, '/html/body/div[4]/p').text
        self.assertEqual(toast_txt, '修改成功')
    #
    def test_0078_alert_mange_setting_xcxbj(self):
        self.login_methon()
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[6]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/button').click()  # 点击警报设置
        elemeng=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[2]/div[2]/span[1]/div/input') # 点击修改状态
        rusult=elemeng.get_attribute("aria-disabled")
        # toast_txt = self.driver.find_element(By.XPATH, '/html/body/div[4]/p').text
        self.assertEqual(rusult, 'true')
    #
    def test_0079_alert_mange_setting_xcxbj(self):
        self.login_methon()
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[6]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/button').click()  # 点击警报设置
        elemeng=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[2]/div[2]/span[2]/div/input') # 点击修改状态
        rusult=elemeng.get_attribute("aria-disabled")
        # toast_txt = self.driver.find_element(By.XPATH, '/html/body/div[4]/p').text
        self.assertEqual(rusult, 'true')
    #
    @file_data("../web_datas/login_datas/add_linkman_data.yaml")
    def test_0085_alert_mange_setting_linkman(self,name,phone_number,status,result):
        """添加短信通知人"""
        self.login_methon()
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[6]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/button').click()  # 点击警报设置
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[3]/div[1]/button').click()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[2]/div/div/div/div/form/div[1]/div/div/div/input').send_keys(name)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[2]/div/div/div/div/form/div[2]/div/div/div/input').send_keys(phone_number)#输入手机好
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[2]/div/div/div/div/form/div[3]/button').click()#点击添加
        sleep(1)
        if status==1:

            eer_info=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[2]/div/div/div/div/form/div[1]/div/div[2]').text
            self.assertEqual(eer_info, result)
        elif status==2:
            eer_info = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[2]/div/div/div/div/form/div[2]/div/div[2]').text
            self.assertEqual(eer_info, result)
        elif status==3:
            eer_info=self.driver.find_element(By.XPATH,'/html/body/div[3]/p').text
            self.assertEqual(eer_info, result)
    #
    def test_0086_alert_mange_del_linkman(self):
        self.login_methon()
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[6]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/button').click()  # 点击警报设置
        try:
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[3]/div[2]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[3]/div/span').click()  # 点击删除
            eer_info = self.driver.find_element(By.XPATH, '/html/body/div[3]/p').text

            self.assertEqual(eer_info,'删除成功')
        except NoSuchElementException as e:
            er=True
            print("没有找到删除按钮",e)
            self.assertEqual(er,'False')

    def test_0087_Renewal_or_recharge_xuqi(self):
        self.login_methon()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[7]').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[3]/button').click()
        try:
            device_name=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div/div[1]/span[1]').text
            device_number=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div/div[1]/span[2]').text
            device_time=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div/div[2]').text
            device_re=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div/div[3]/div/div').text
            print("点击续期后显示的文本：\n{}\n{}\n{}\n{}".format(device_name,device_number,device_time,device_re))
        except:
            print("你的设备是免资费版本")

    def test_0088_Renewal_or_recharge_record(self):
        data=[]
        self.login_methon()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[7]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[1]/button').click()
        element=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody')
        content=element.find_elements(By.TAG_NAME,'tr')
        for i in content:
            data.append(i.text)
        print(data)
    #
    def test_0089_Renewal_or_recharge_sms(self):

        self.login_methon()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[7]').click()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div[3]/button').click()
        sms_info=self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[4]/div/div/div/div/div/div[1]/div').text
        print(sms_info)

    def test_0090_Renewal_or_recharge_sms_record(self):
        data=[]
        self.login_methon()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[7]').click()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/div[1]/button').click()
        try:
            element = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div[3]/div/div[1]/div/table/tbody')
            content=element.find_elements(By.TAG_NAME,'tr')
            for i in content:
                data.append(i.text)
            print(data)
        except :
            print("当前没有短信充值记录")






    def tearDown(self):
        sleep(1)
        self.driver.quit()
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()



if __name__ == '__main__':
    unittest.main()
