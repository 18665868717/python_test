# import requests
#
from locust import HttpUser, task, between, TaskSet
import requests

def login_001():
    """该函数只会运行一次"""
    login_url = "https://tuyingtest.mncats365.com/webApi/login"
    login_data = {"phoneNum": '18665868717', "pass": '123456'}
    response = requests.get(login_url, params=login_data,)
    token = response.json()["data"]["token"]
    return token
class login_test(TaskSet):
    """测试任务集"""
    # def on_start(self):
    #     self.client.truse_env=False

    @task
    def my_task(self):

        datas= {"needShare": "true","token":self.parent.token}
        response = self.client.post("/device/findByUserId",data=datas,name='查询用户设备').json()
        assert response["statusMsg"]=="查询成功"

class MyUser(HttpUser):
    tasks = [login_test]
    host = 'https://tuyingtest.mncats365.com'
    token = login_001()
    wait_time = between(0,3)




