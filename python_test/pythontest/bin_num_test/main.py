import xlrd
import  os
import json
import datetime
import paho.mqtt.client as mqtt
binum=1011004
binver="1.11.4"

def get_file_names():
    path = os.getcwd()
    file_path = path + "/datas/"
    file_names = os.listdir(file_path)
    file_name_pata = file_path + file_names[0]
    return file_name_pata
def red_file():
    file_name_path=get_file_names()
    file_datas=xlrd.open_workbook(file_name_path)
    file_oj=file_datas.sheet_by_index(0)
    column_sum=file_oj.nrows #获取整个列的数量
    for i in range(1,column_sum):
        result_mac=file_oj.cell_value(i,2) # 第一个参数是列，第二个参数行
        result_tyoe=file_oj.cell_value(i,5) # 第一个参数是列，第二个参数行
        result_binver=file_oj.cell_value(i,4) # 第一个参数是列，第二个参数行
        result_moving_stutas=file_oj.cell_value(i,10) # 第一个参数是列，第二个参数行
        result_iccid=file_oj.cell_value(i,7) # 第一个参数是列，第二个参数行
        if len(result_mac)==12:
            if result_tyoe =="GPSV2":
                if int(result_binver) != binum:
                    if int(result_moving_stutas)==0:
                        if len(result_iccid) >18:
                            Operating_mqtt(result_mac)
                    # print(result_mac,result_tyoe,result_binver)

def Operating_mqtt(result_mac):
    now = datetime.datetime.now()
    host="emqxserver.mncats365.com"
    port=1883
    username="gpspack"
    password="ZkaxPack20220114"
    topic="sticks/"+result_mac
    body={"a":7,"b":{"ag":"GPSV2","ah":binum,
    "ai":"https://mncats-pub.oss-cn-shenzhen.aliyuncs.com/BinUpdate/GpsStickerTest/GPSV2/1.11.4/car_locator1.11.4_1011005_test_ota.bin",
    "k":binver},"g":now.strftime("%Y%m%d%H%M%S"+"737")}
    client=mqtt.Client()
    client.username_pw_set(username,password)
    client.connect(host=host,port=port)
    datas=json.dumps(body)
    client.publish(topic,datas,2)
    print(topic,"发送的body是："+datas)
if __name__ == '__main__':
    red_file()