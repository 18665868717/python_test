import requests
from wxpusher import WxPusher  # https://github.com/wxpusher/wxpusher-sdk-python

app_token = 'AT_zUhnfENXmibCIuir9Rb9NTI2xtbUcFNa'  # 本处改成自己的应用 APP_TOKEN
uid_myself = 'UID_V6HNRYza7Yrta4Ixm1Te6nOZyNG4'  # 本处改成自己的 UID


def wxpusher_send_by_webapi(msg):
    """利用 wxpusher 的 web api 发送 json 数据包，实现微信信息的发送"""
    webapi = 'http://wxpusher.zjiecode.com/api/send/message'
    data = {
        "appToken": app_token,
        "content": msg,
        "summary": msg[:99],  # 该参数可选，默认为 msg 的前10个字符
        "contentType": 1,
        "uids": [uid_myself, ],
    }
    result = requests.post(url=webapi, json=data)
    return result.text


def wxpusher_send_by_sdk(msg):
    """利用 wxpusher 的 python SDK ，实现微信信息的发送"""
    result = WxPusher.send_message(msg,
                                   uids=[uid_myself, ],
                                   token=app_token,
                                   summary=msg[:99])
    return result


def main(msg):
    # result1 = wxpusher_send_by_webapi(msg)
    result2 = wxpusher_send_by_sdk(msg)
    # print(result1)
    print(result2)


if __name__ == '__main__':
    main('预购失败!')
