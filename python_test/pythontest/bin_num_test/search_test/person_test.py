import requests
from bs4 import BeautifulSoup
import json
url='https://peoplesearch.com/search?s_name=Edward+Snowden&s_loc='
response=requests.get(url=url)
content=response.content
soup=BeautifulSoup(content,'html.parser')

class_name='text-ps-black bg-white 2xl:ml-3 gap-3 grid grid-cols-1 hover:bg-ps-white hover:ring-1 hover:ring-inset hover:ring-ps-grey-border hover:shadow-lg lg:ml-6 lg:mr-3 lg:mx-0 lg:p-6 mb-6 md:grid-cols-4 md:p-6 p-3 rounded-none shadow-md sm:mx-6 sm:p-4 sm:rounded-xl'
all_people=soup.find_all('div',class_=class_name)
# print(len(all_people))
person_all={}
another_name=[]
age=""
current_address=""
Other_addresses=""
relatives=""
num = 1
people={}
for i in all_people:
    # print(i)
    info="people"+str(num)
    info={}
    name=i.find('h2').string
    info["name"]=name
    # print(info)
    age = i.find_all_next('span', class_="font-medium")

    print(age)
    # print(age[0].text)

    var_data=[]
    biecheng=i.find('span',class_="text-sm text-gray-500")
    for j in biecheng:
        name_len=j.text
        if len(name_len) >2:
            var_data.append(name_len)
    info["onther_name"]=var_data

    addr=[]
    this_address=i.find_all('div',class_="whitespace-nowrap overflow-hidden text-ellipsis")
    for k in this_address:
        addr_text=k.text
        addr.append(addr_text)
    info["current_address"]=addr

    # print(info)
    """其他位置"""
    qita_addr=i.find_all('div',class_="flex flex-col")[1]
    addr_other=qita_addr.find_all('div', class_="whitespace-nowrap overflow-hidden text-ellipsis my-1 pl-2")
    # print(qita_addr)
    data=[]
    for q in addr_other:
        test_add=q.text
        data.append(test_add)
    info["other_locations"]=data


    relatives_data=[]
    relative_all=i.find_all('div',class_="flex flex-col")[2]
    # print(relative_all)
    relatives=relative_all.find_all('div', class_="whitespace-nowrap overflow-hidden text-ellipsis my-1 pl-2")
    # print(relatives)
    for w in relatives:
        ooo=w.text
        relatives_data.append(ooo)
    info["relatives_or_number"]=relatives_data

    person_all["person"+str(num)]=info
    num = num + 1

with open('data.json', 'w') as file:
    file.write(json.dumps(person_all))

