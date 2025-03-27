from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import re
from components.Mobile import element_exist_uiautomator, get_dv_topic_list, get_dv_content, wait_element_xpath,wait_element_uiautomator
from components.Mobile import element_exist_uiautomator, get_dv_topic_list, print_source, wait_element_xpath
from components.Mobile import GestureUnlock
import time
from xml.dom.minidom import parseString, parse #导入解析字符串的包


def TencentFortune():
    # 配置信息
    desired = {
        "platformName": "Android",
        "platformVersion": "10.0.0",
        "deviceName": "D3H0217B25000844",
        "appPackage": "com.tencent.fortuneplat",
        # "appActivity": ".password.gesturelock.GuestureUnLockActivity",
        "appActivity": "com.tencent.fortuneplat.login_impl.SplashActivity",
        "noReset": True,
        "automationName": 'uiautomator2',
        "newCommandTimeout": 6000,
        "unicodeKeyboard": True,
        "resetKeyboard": True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired)
    resolution = driver.get_window_size()
    print(f'手机屏幕分辨率: {resolution}')

    # 解锁屏幕
    GestureUnlock(driver)

    # 1.稳健理财
    path_wjlc_button = 'new UiSelector().text("稳健理财")'
    if element_exist_uiautomator(driver, path_wjlc_button):
        element1 = driver.find_element_by_android_uiautomator(path_wjlc_button)
        element1.click()
        print(f'点击: 稳健理财')
    else:
        print('稳健理财定位失败')

    # 1.1 安稳理财-查看更多
    path_wjlc_more = 'new UiSelector().text("查看更多")'
    time.sleep(2)
    if element_exist_uiautomator(driver, path_wjlc_more):
        element_wjlc_more = driver.find_element_by_android_uiautomator(path_wjlc_more)
        element_wjlc_more.click()
        print(f'点击: 安稳理财-查看更多')
    else:
        print('安稳理财-查看更多, 定位失败')
    time.sleep(2)

    # 滑动屏幕设置
    screen_width = resolution['width']
    screen_height = resolution['height']
    start_x_percent = 0.5
    start_y_percent = 0.9
    end_x_percent = 0.5
    end_y_percent = 0.2
    start_x = int(screen_width * start_x_percent)
    start_y = int(screen_height * start_y_percent)
    end_x = int(screen_width * end_x_percent)
    end_y = int(screen_height * end_y_percent)

    # 保存数据的列表
    scroll_count = 0
    last_title = ""  # 保存最后一个title

    while True:
        # 执行滑动操作
        print('执行滑动操作')
        driver.swipe(start_x, start_y, end_x, end_y, duration=4000)  # 持续时间可根据需要进行调整

        # 获取当前屏幕的数据并保存
        path_wjlc = 'new UiSelector().className("android.view.View").textContains("+")'
        # element_wjlc = driver.find_elements_by_android_uiautomator(path_wjlc)
        # if wait_element_uiautomator(driver, path_wjlc, 60):
        # path_wjlc = 'new UiSelector().className("android.view.View")'
        # element_wjlc = driver.find_elements_by_android_uiautomator(path_wjlc)

        xml_string = driver.page_source  # 解析文档
        # get_dv_content(xml_string)  # 获取数据

        DOMTree = parseString(xml_string)  # 解析xml, 得到dom树
        collection = DOMTree.documentElement  # 文档的根元素节点
        nodes = collection.getElementsByTagName("android.view.View")
        pattern = r"\+.*%$"
        txt_list = []

        for node in nodes:
            node_text = str(node.getAttribute('text'))       # 所有节点数据
            print(f'node_text: {node_text}')
            match = re.match(pattern, node_text)             # 匹配3.78%
            print(f'match: {match}')

            if len(node_text) > 0 and node_text != "\n" and match:
                try:
                    # 以node_text为起点 获取各个节点数据
                    print(f'{node_text}为起点 获取各个节点数据')
                    title = node.parentNode.previousSibling.previousSibling.previousSibling.previousSibling.previousSibling.previousSibling.getAttribute('text')
                    holding_time = node.nextSibling.nextSibling.nextSibling.nextSibling.getAttribute('text')
                    transaction_cost = node.parentNode.previousSibling.previousSibling.getAttribute('text')
                    risk_level = node.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.getAttribute('text')

                    # node_text坐标
                    bounds_txt = str(node.getAttribute('bounds'))
                    bounds_txt = re.findall("(\d{1,4})", bounds_txt)

                    # 保存到字典
                    item = {
                        "row_txt": node_text,
                        "bounds": bounds_txt,
                        'title': title,
                        'transaction_cost': transaction_cost,
                        'risk_level':risk_level,
                        'holding_time': holding_time
                    }

                    txt_list.append(item)
                except Exception as e:
                    print(e)
        # 将数据保存到总列表
        print(f'txt_list: {txt_list}')
        # data_list.extend(txt_list)


        # 检查是否滑动到了页面底部

        if last_title == title:
            print('已经滑动到了底部')
            break  # 页面没有发生变化，说明已经滑动到了底部

        last_title = title

        scroll_count += 1
        if scroll_count >= 10:  # 设置滑动次数上限，避免无限滑动
            break
    print(f'txt_list: {txt_list}')

    # 输出保存的数据
    # for data in data_list:
    #     print(data)

    driver.quit()
if __name__ == '__main__':
    TencentFortune()
