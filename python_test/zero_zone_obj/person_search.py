import requests
from bs4 import BeautifulSoup
url='https://peoplesearch.com/search?s_name=Edward+Snowden&s_loc='
response=requests.get(url=url)
content=response.content
soup=BeautifulSoup(content,'html.parser')
result=soup.select('body div:nth-of-type(2) div:nth-of-type(2) div div:nth-of-type(3)')
print(result)
# print(soup)
# class_name='text-ps-black bg-white 2xl:ml-3 gap-3 grid grid-cols-1 hover:bg-ps-white hover:ring-1 hover:ring-inset hover:ring-ps-grey-border hover:shadow-lg lg:ml-6 lg:mr-3 lg:mx-0 lg:p-6 mb-6 md:grid-cols-4 md:p-6 p-3 rounded-none shadow-md sm:mx-6 sm:p-4 sm:rounded-xl'
# all_people=soup.find('div',class_=class_name)

# name1=all_people.find('h2').string
# print(name1)
"""获取别称"""
# biecheng=all_people.find('span',class_="text-sm text-gray-500")
# for i in biecheng:
#     name_len=i.text
#     if len(name_len) >2:
#         print(name_len)

"""获取年龄"""
# age=all_people.find_all('span',class_='font-medium')[1].text
# print(age)

"""获取当前地址"""
# this_address=all_people.find_all('div',class_="whitespace-nowrap overflow-hidden text-ellipsis")
# for i in this_address:
#     addr_text=i.text
#     print(addr_text)
"""其他地址"""
# qita_addr=all_people.find_all('div',class_="flex flex-col")[1]
# addr_other=qita_addr.find_all('div', class_="whitespace-nowrap")
# for i in addr_other:
#     other_addr=i.text
#     print(other_addr)
"""获取亲属们"""
# relative_all=all_people.find_all('div',class_="flex flex-col")[2]
# relatives=relative_all.find_all('div', class_="whitespace-nowrap overflow-hidden text-ellipsis my-1 pl-2")
# for i in relatives:
#     ooo=i.text
#     print(ooo)
"""获取手机信息"""
# phone_all=all_people.find_all('div',class_="flex flex-col")[3]
# numbers=phone_all.find_all('div', class_="whitespace-nowrap overflow-hidden text-ellipsis my-1 pl-2")
# for i in numbers:
#     number=i.text
#     print(number)