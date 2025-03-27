from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# driver.implicity_wait(10)

driver.get('https://myplugin.speedtest.cn/#/')
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div').click()

while True:
    sleep(1)
    try:
        element=driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div')
        element.click()
        # break
    except:
        print("没有找到元素")


# driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/p').click()
# driver.find_element(By.CSS_SELECTOR,'form#login>div>div>div>div>input').clear()
# driver.find_element(By.CSS_SELECTOR,'form#login>div>div>div>div>input').send_keys(18665868717)
# driver.find_element(By.CSS_SELECTOR,'#login>div:nth-child(2)>div>div>div>input').clear()
# driver.find_element(By.CSS_SELECTOR,'#login>div:nth-child(2)>div>div>div>input').send_keys(111111)
# driver.find_element(By.XPATH,'//*[@id="login"]/div[4]').click()
# table_all=driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[3]/div[1]/div[2]/table')
# content_h=driver.find_elements(By.TAG_NAME,"td")
# # print(table_all)
# # print(content_h.text)
# for i in content_h:
#     arr1=(i.text).split(" ")
#     arr.append(arr1)
# n = 3 # 表示多少个一组
# for list in [arr[i:i + n] for i in range(0, len(arr), n)]:
#     # sehi=list[0]
#     print(list[:])


# print(list_da
