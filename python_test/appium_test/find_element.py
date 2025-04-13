from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import os

class BaseAction():
    def __init__(self,driver):
        self.driver=driver
    #显示等待
    def find_element(self,loc,time=30,poll=1):
       return WebDriverWait(self.driver,time,poll).until(lambda x: x.find_element(*loc))

    #显示等待，返回列表
    def find_elements(self,loc,time=30,poll=1):
       return WebDriverWait(self.driver,time,poll).until(lambda x: x.find_elements(*loc))

    #点击方法
    def click(self,loc):
        self.find_element(loc).click()

    #输入方法
    def input(self,loc,value):
        self.find_element(loc).send_keys(value)
    #获取元素对应的值
    def resource_text(self,loc):
       return self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId('+loc+')')

    #获取文本方法
    def get_text(self,loc):
        return self.find_element(loc).text

    def Switch_the_input_method(self,loc,value):
        os.system("adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
        self.input(loc,value)
        os.system("adb shell ime set io.appium.settings/.UnicodeIME")


    def long_hold(self,loc,):
        """此方法还需要改进"""
        #长按一个元素方法
        action = TouchAction(self.driver)
        el = self.find_element(loc)
        action.long_press(el).wait(10000).release().perform()

    #截图方法
    def get_image(self):
        self.driver.save_screenshot('./image/login.png')


    #切换输入法输入bin搜索
    # def Switch_the_input_method(self,loc,value,time=30,poll=1):
    #     os.system("adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
    #     input_value=WebDriverWait(self.driver, time, poll).until(lambda x: x.find_element(*loc))
    #     input_value.send_keys(value)
    #     os.system("adb shell ime set io.appium.settings/.UnicodeIME")


    #向上滑动方法
    def up_roll(self):
        width=self.get_resolution_width()
        height=self.get_resolution_height()
        self.driver.swipe(start_x=width*0.5,start_y=height*0.1,end_x=width*0.5,end_y=height*0.9)

    #向下滑动方法
    def down_roll(self):
        width = self.get_resolution_width()
        height = self.get_resolution_height()
        self.driver.swipe(start_x=width * 0.5, start_y=height * 0.9, end_x=width * 0.5, end_y=height * 0.1)

    #向左滑动方法
    def left_roll(self):
        width = self.get_resolution_width()
        height = self.get_resolution_height()
        self.driver.swipe(start_x=width * 0.9, start_y=height * 0.5, end_x=width * 0.1, end_y=height * 0.5)

    #向右滑动方法
    def right_roll(self):
        width = self.get_resolution_width()
        height = self.get_resolution_height()
        self.driver.swipe(start_x=width * 0.1, start_y=height * 0.5, end_x=width * 0.9, end_y=height * 0.5)


    #获取手机宽度分辨率
    def get_resolution_width(self):
        size=self.driver.get_window_size()
        return size["sidth"]

    #获取手机高度分辨率
    def get_resolution_height(self):
        size=self.driver.get_window_size()
        return size["height"]

    #打开手机WiFi
    def open_wifi(self):
        os.system('adb shell svc wifi enable')

    #关闭手机WiFi
    def close_wifi(self):
        os.system('adb shell svc wifi disable')