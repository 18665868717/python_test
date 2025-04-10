import json
import random
import time

from locust import User, between, task, constant
import socket

class UDPUser(User):
    wait_time = between(1, 2)
    host = "192.168.0.20"
    port = 8083


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((self.host, self.port))

    @task
    def send_udp(self):
        #"P:FD:AB:79:08:7D:8C"
        id=random.randint(17,18)
        tag_id="P:FD:AB:79:08:7D:"+str(hex(id)).upper()[2:]
        loID="FDAB79087D"+str(hex(id)).upper()[2:]
        data={"device":"E05A1BA8969C","data":"EXT0:ALwgCHmr/QEC0P0AAAEAUlTqLErCP6/YEKhX+xlSsyzts0zcx/IVpFMxVZw1SdxSCVWz7AGq3Cy/v1XT2IBg+B5URDPAKr3ECjGkDBKfhtAwr1oGSdMMSq4ZMg7YUrTAnlTSqzC2/6ZGFu9SJtU3Q6YkFn2i/tCutNQ4y0Mw8MhV5f1ffxvVV6UPuzTjt0bQxvkKplwfP4tMOPVZKUm0D9mv+Dai9iCljL45slsLTNgMSq4g"}
        # message =json.dumps(data)
        # message =data
        # print(message)
        # self.sock.sendto(data.encode(), (self.host, self.port))
        # time.sleep(1)

        data = bytes(json.dumps(data), encoding='utf-8')
        # 发送消息到服务器
        self.sock.sendall(data)


    def on_stop(self):
        self.sock.close()

class MyTestLocust(UDPUser):
    min_wait = 5000
    max_wait = 15000