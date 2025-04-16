from web_beas.base_action import BaseAction
from selenium.webdriver.common.by import By

class Add_Imsi_Page(BaseAction):

    common_yanpan = By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView"
    mubiao_bukong =By.ID,"com.isen.macimsihdml.test:id/traceView"
    click_jiahao_button= By.ID,"com.isen.macimsihdml.test:id/add"
    click_add_imsi_button=By.ID,"com.isen.macimsihdml.test:id/addTraceImsi"
    imsi_input_info = By.ID,"com.isen.macimsihdml.test:id/macEdit"
    imsi_info_comfirm=By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[2]"
    def click_yanpan(self):
        self.click(self.common_yanpan)
    def click_guanzhu_bukong(self):
        self.click(self.mubiao_bukong)
    def click_add_jiahao(self):
        self.click(self.click_jiahao_button)
    def click_add_imsi(self):
        self.click(self.click_add_imsi_button)
    def input_imsi(self,IMSI):
        self.input(self.imsi_input_info,IMSI)
    def click_confirm(self):
        self.click(self.imsi_info_comfirm)
    def imsi_yewu_zuhe(self,IMSI):
        self.click_yanpan()
        self.click_guanzhu_bukong()
        self.click_add_jiahao()
        self.click_add_imsi()
        self.input_imsi(IMSI)
        self.click_confirm()