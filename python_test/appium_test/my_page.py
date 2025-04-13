from find_element import BaseAction
from selenium.webdriver.common.by import By


class Login_Page(BaseAction):
    login_input_phonr = By.ID, 'com.isen.macimsihdml.test:id/userPhone'
    login_input_pass = By.ID, "com.isen.macimsihdml.test:id/userPass"
    login_login_button = By.ID, "com.isen.macimsihdml.test:id/login"
    lonin_info=By.ID,"com.isen.macimsihdml.test:id/message"
    login_info_confirm=By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button"


    login_click_tishi=By.ID,"com.isen.macimsihdml.test:id/guide_welcome_check"
    login_guide_skip =By.ID,"com.isen.macimsihdml.test:id/guide_btn_skip"



    def input_phone(self,phone):
        self.input(self.login_input_phonr,phone)
        print(self.login_input_phonr)

    def input_password(self,password):
        self.input(self.login_input_pass,password)

    def click_button(self):
        self.click(self.login_login_button)


    def click_login_info_confrim(self):

        try:
            # self.find_element(self.login_info_confirm)
            self.click(self.login_info_confirm)

        except:
            self.click(self.login_click_tishi)
            self.click(self.login_guide_skip)



    # def is_element_exist(element,timeout=1):
    #     count = 0
    #     while count < timeout:
    #         souce = driver.page_source
    #         if element in souce:
    #             return  True
    #         else:
    #             count += 1
    #             time.sleep(1)
    #     return False


    def yewu_zuhe(self,phone,password):
        self.input_phone(phone)
        self.input_password(password)
        self.click_button()
        # self.get_login_info()
        self.click_login_info_confrim()
