import requests
from bs4 import BeautifulSoup
import sys
import json
person_all={}
null_data={}
num=1
def get_url(name):
    url="https://clustrmaps.com/persons/"+name
    header={
        #"Sec-Fetch-Mode":"navigate",
        #"Sec-Ch-Ua":'Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115',

            "Content-Type":"text/json;charser=utf-8",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Referer":"https://clustrmaps.com/",
            "Sec-Ch-Ua":"Google Chrome",
            #"Upgrade-Insecure-Requests":"1",
            #"Sec-Ch-Ua-Platform":"Windows",
            #"Sec-Fetch-Dest":"document",
            #"Referer":"https://clustrmaps.com/a/?__cf_chl_tk=Q5z2YqLGc1p2TeDnmoLaYKPOlXzgkZ2LmeRW1MOfDy0-1690204900-0-gaNycGzNCns",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",

            }
    cookie={"Set-Cookie":'fse_--DbOgkHVf6S0A_iDklyFnOKWDrQKqtFbGE4pHs'}
    response=requests.get(url=url,headers=header,cookies=cookie)
    return response.content
def write_json(data_name):
    with open("./clustrmaps_person.json", "w", encoding='utf-8')as f:
        f.write(json.dumps(data_name))

def read_txt():
    with open("./clustrmaps.txt", "r", encoding='utf-8')as f:
        content=f.read()
        return content
def data_process(data):
    global person_all
    global num
    soup = BeautifulSoup(data, 'html.parser')
    print(soup)
    parnet_node= soup.find_all('div',class_="mb-5")
    for i in parnet_node:
        info="people"+str(num)
        info={}
        try:
            names=i.find('span',itemprop="name")
            na=names.text
            info["name"]=na
        except:
            info["name"]="none"

        """年龄"""
        try:
            ages=i.find('span',class_='age')
            ag=ages.text
            info["age"]=ag
        except:
            info["age"] = "null"

        """地址信息"""
        try:
            addr=i.find('span',itemprop="streetAddress")
            addre=addr.text
            info["address"]=addre
        except:
            info["address"] = "null"

        """其他名字"""
        try:
            nick_names = i.find('div',class_='i_aka')
            an_name=nick_names.text
            info["another_name"]=an_name
        except:
            info["another_name"]="null"

        """相关的联系人"""
        try:
            relatives = i.find('div', class_='i_people')
            rele_name=relatives.text
            info["relevant_person"]=rele_name
        except:
            info["relevant_person"]="null"

        """联系电话"""
        try:
            phones = i.find('span',itemprop="telephone")
            ph=phones.text
            info["phone_number"]=ph
        except:
            info["phone_number"] = "null"
        person_all["person"+str(num)]=info
        # print(person_all)
        num=num+1
    write_json(person_all)
    # print(person_all)
if __name__ == '__main__':
    args=sys.argv
    search_name=args[1]
    try:
        response=get_url(search_name)
        data_process(response)
    except:
        write_json(null_data)