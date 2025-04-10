# import minium
# mini = minium.Minium({
#     "project_path": "/Users/isentech/Desktop/微信开发/",   # 替换成你的【小程序项目目录地址】
#     "dev_tool_path": "/Applications/wechatwebdevtools.app/MacOS/cli",
#     "platform": "ide"# 替换成你的【开发者工具cli地址】，macOS: <安装路径>/Contents/MacOS/cli， Windows: <安装路径>/cli.bat
# })
# print(mini.get_system_info())
# # "/Applications/wechatwebdevtools.app/MacOS/cli" auto --project "/Users/isentech/Desktop/微信开发/" --auto-port 9420

import minium
import device_config as  de
from time import sleep


import minium
class FirstTest(minium.MiniTest):
    # "device_desire": {"serial": "181QGEYG2249J"},
    def setUp(self) -> None:
        pass

    def test_01_bing_device(self):
        """空设备进入小程序，进入添加设备页面"""
        self.page.wait_for(2)
        page=self.page.path
        self.assertEqual(page,"/pagesDevice/addDevice/addDevice")

    def test_02_add_device_index(self):
        """添加完设备，首页确定设备存在"""
        self.page.wait_for(2)
        self.page.get_element("/page/view/view[3]/view[1]/view[1]/view/view/view/view/view/view/view[1]/input").input(de.device_mac_01)
        self.page.get_element("/page/view/view[3]/view[1]/view[2]/view/view/view/view/view/view/view/input").input(de.device_name_01)
        self.page.get_element("/page/view/view[3]/view[2]/button").click()
        self.page.get_element("/page/view/view[3]/view[4]/button").click()
        self.app.go_home("/pages/index/index")
        # page = self.page.get_element('//*[@id="listDOM"]/device-item/view/view[1]')
        # self.assertTrue(page,msg='没找到首页设备列表的元素')
    def test_03_click_loc(self):
        self.page.wait_for(2)
        self.page.get_element('//*[@id="devicePopup"]/view[7]/locate-button/view').click()

    def test_04_click_navigation(self):
        self.page.wait_for(2)
        self.page.get_element('//*[@id="devicePopup"]/view[7]/view[1]').click()
        path=self.page.path
        self.assertEqual(path,'/pagesIndex/navigation/navigation')
        self.app.go_home("/pages/index/index")

    def test_05_click_Precise_positioning(self):
        pass
    def test_06_click_historical_track(self):
        self.page.wait_for(2)
        self.page.get_element('//*[@id="devicePopup"]/view[7]/view[2]').click()
        page=self.page.path
        self.assertEqual(page,'/pagesIndex/historicalRoute/historicalRoute')
        self.app.go_home("/pages/index/index")


    def test_07_to_device_page(self):
        """进入设备导航栏"""
        # self.app.go_home()
        self.app.switch_tab('/pages/device/device')
        sleep(3)


    def test_08_auto_add_device(self):
        """自动添加设备，判断是否能正常进入自动添加设备页面"""
        self.page.get_element('#shouUi').click()
        self.page.get_element('//*[@id="menuList"]/view[1]').click()
        page=self.page.path
        self.assertEqual(page,'/pagesDevice/smartAddDevice/smartAddDevice')
        self.app.go_home("/pages/index/index")
        self.app.switch_tab('/pages/device/device')

    # def test_09_manual_add_device(self):
    #     """手动添加时设备"""
    #     self.page.wait_for(2)
    #     self.page.get_element('//*[@id="showUi"]/button').click()
    #     self.page.get_element('//*[@id="menuList"]/view[2]').click()
    #     self.page.get_element('/page/view/view[3]/view[1]/view[1]/view/view/view/view/view/view/view[1]/input').input(de.device_mac_02)
    #     self.page.get_element('/page/view/view[3]/view[1]/view[2]/view/view/view/view/view/view/view/input').input(de.device_name_02)
    #     self.page.get_element('/page/view/view[3]/view[2]/button').click()
    #     self.page.get_element('/page/view/view[3]/view[4]/button').click()
    #     self.app.go_home("/pages/index/index")
    #     self.app.switch_tab('/pages/device/device')
    #
    # def test_10_single_unbing(self):
    #     pass
    #     # self.page.get_element('/page/view/view[2]/button').click()
    #
    #     # device_list=self.page.get_elements('.device')  设备页面获取所有设备返回list
    # def test_11_all_unbing_device(self):
    #     self.page.get_element('/page/view/view[2]/button').click()
    #     self.page.get_element('/page/view/view[4]/view[1]/my-check-box/view').click()
    #     self.page.get_element('/page/view/view[4]/view[2]').click()
    #     self.page.get_element('/page/view/view[4]/view[2]').click()
    #
    #
    # def test_12_alarm_msg(self):
    #     pass
    #
    #



