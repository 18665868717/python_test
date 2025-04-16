# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
#
# # 创建 ChromeOptions 对象，设置无头模式
# chrome_options = Options()
# chrome_options.add_argument('--headless')
#
# # 创建 Service 对象，指定 ChromeDriver 路径和 ChromeOptions 对象
# service = Service('/usr/local/chromedriver.exe', options=chrome_options)
#
# # 启动 ChromeDriver
# service.start()
#
# # 创建 ChromeDriver 对象，指定 Service 对象
# driver = webdriver.Chrome(service=service)
#
# # 打开网页
# driver.get('https://www.baidu.com')
# print(driver.current_url)
# # 进行各种操作，比如查找元素、填写表单等
# ...
#
# # 关闭浏览器窗口和 ChromeDriver
# driver.quit()
# service.stop()

#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
#
# # 创建 ChromeOptions 对象，设置无头模式
# chrome_options = Options()
# chrome_options.add_argument('--headless')
#
# # 创建 Service 对象，指定 ChromeDriver 路径和 ChromeOptions 对象
# service = Service('/usr/local/bin/chromedriver.exe', options=chrome_options)
#
# # 启动 ChromeDriver
# service.start()
#
# # 输出 ChromeDriver 的日志信息（可选）
# print()
#
# # 创建 ChromeDriver 对象，指定 Service 对象
# # driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome(chrome_options=options)
#
# # 打开网页
# driver.get('https://www.baidu.com')
#
# # 获取当前页面的 URL
# current_url = driver.current_url
#
# # 输出当前页面的 URL
# print(current_url)
#
# # 关闭浏览器窗口和 ChromeDriver
# driver.quit()
# service.stop()




from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# 通过driver.get()来打开对应链接
driver.get(url="https://www.baidu.com/")

print(driver.current_url)
#
# from time import sleep
# from selenium import webdriver
#
# def test():
#     driver = webdriver.Chrome()
#     driver.get('http://www.baidu.com')
#     print(driver.current_url)
#     sleep(4)
# if __name__ == '__main__':
#     test()
