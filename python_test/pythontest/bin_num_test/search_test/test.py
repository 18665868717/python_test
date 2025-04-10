import requests
from bs4 import BeautifulSoup
import sys
import json
person_all={}
null_data={}
num=1
def get_url(name):
    url="https://clustrmaps.com/persons/"+name
    response=requests.get(url=url)
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

        """获取home"""
        try:
            names=i.find('div',class_="person_city")
            na=names.text
            info["home"]=na
        except:
            info["home"]="null"

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
    # args=sys.argv
    # search_name=args[1]
    content=read_txt()
    data_process(content)



