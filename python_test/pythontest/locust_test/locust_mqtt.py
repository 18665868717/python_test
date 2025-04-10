import time
import random
import string
import paho.mqtt.client as mqtt

# MQTT服务器的地址和端口
broker_address = "mqtt.example.com"
broker_port = 1883

# MQTT客户端的ID
client_id = ''.join(random.choice(string.ascii_letters) for i in range(10))

# 订阅的主题
subscribe_topic = "test/topic"

# 发布的主题
publish_topic = "test/topic"

class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client(client_id=client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set()
        self.client.connect(broker_address, broker_port)
        self.messages_received = 0

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe(subscribe_topic)

    def on_message(self, client, userdata, msg):
        print("Received message: " + msg.payload.decode())
        self.messages_received += 1

    def publish_message(self, message):
        self.client.publish(publish_topic, message)

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()

# 实例化 MQTTClient
mqtt_client = MQTTClient()

# 启动 MQTTClient
mqtt_client.start()

# 发布消息
mqtt_client.publish_message("Hello, MQTT!")

# 等待一段时间
time.sleep(10)

# 停止 MQTTClient
mqtt_client.stop()
from locust import User, task, between


class MyUser(User):
    wait_time = between(1, 3)

    def on_start(self):
        # 实例化 MQTTClient
        self.client = MQTTClient()
        # 启动 MQTTClient
        self.client.start()

    def on_stop(self):
        # 停止 MQTTClient
        self.client.stop()

    @task
    def publish_message_task(self):
        # 发布消息
        self.client.publish_message("Hello, MQTT!")

# 运行 Locust 压测
if __name__ == "__main__":
    MyUser().run()