
import random
# id=random.randint(0,201)
import requests

for i in range(17,218):
    # data=str(hex(i))
    # dat=
    tag_id="P:FD:AB:79:08:7D:"+str(hex(i)).upper()[2:]
    # print(tag_id)
    data={
        "remarks":"",
        "tagId": tag_id,
        "userId":"",
        "userName":"",

    }
    headers = {"Content-Type": "application/json"}
    content=requests.post(url='http://btaoa.mncats365.com/tag/add?token=905B81B4DFE35516CA9DF5303F7BA7C4&userId=1',json=data,headers=headers)
    print(content)
