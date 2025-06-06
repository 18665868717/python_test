# from locust import HttpUser, task, between, TaskSet
# import random
# import csv
# import queue

URL="https://tuying.mncats365.com/webApi/login?phoneNum=18665868717&pass=123456"

# # ---------------------------
# # 账号池初始化 & 拆分
# # ---------------------------
# def load_and_split_accounts(file_path):
#     with open(file_path, 'r') as f:
#         reader = csv.reader(f)
#         all_accounts = list(reader)
#     random.shuffle(all_accounts)
#     return {
#         "login": queue.Queue(),
#         "browse": queue.Queue(),
#         "cart": queue.Queue(),
#         "pay": queue.Queue()
#     }, {
#         "login": all_accounts[:2000],
#         "browse": all_accounts[2000:6000],
#         "cart": all_accounts[6000:8000],
#         "pay": all_accounts[8000:10000]
#     }
#
# # 初始化账号池和分配
# account_queues, grouped_accounts = load_and_split_accounts("accounts.csv")
# for k in account_queues:
#     for acc in grouped_accounts[k]:
#         account_queues[k].put(acc)
#
# # ---------------------------
# # 基础用户类：登录 + Token
# # ---------------------------
# class AuthenticatedUser(HttpUser):
#     wait_time = between(1, 2)
#     user_type = ""  # 子类里设置为 login / browse / cart / pay
#
#     def on_start(self):
#         retry = 3
#         while retry > 0:
#             try:
#                 username, password = account_queues[self.user_type].get_nowait()
#                 res = self.client.post("/api/login", json={
#                     "username": username,
#                     "password": password
#                 })
#
#                 if res.status_code == 200 and "token" in res.json():
#                     token = res.json()["token"]
#                     self.client.headers.update({
#                         "Authorization": f"Bearer {token}"
#                     })
#                     break
#                 else:
#                     retry -= 1
#                     print(f"❌ 登录失败：{username}, 状态码 {res.status_code}")
#             except queue.Empty:
#                 print(f"⚠️ 没有更多账号用于 {self.user_type}")
#                 break
#
# # ---------------------------
# # 不同行为的用户类
# # ---------------------------
#
# class LoginUser(AuthenticatedUser):
#     user_type = "login"
#
#     @task
#     def do_nothing(self):
#         pass  # 登录后不做操作
#
#
# class BrowseUser(AuthenticatedUser):
#     user_type = "browse"
#
#     @task(2)
#     def browse_products(self):
#         self.client.get("/api/products")
#
#     @task(1)
#     def view_detail(self):
#         self.client.get(f"/api/products/{random.randint(1000, 2000)}")
#
#
# class CartUser(AuthenticatedUser):
#     user_type = "cart"
#
#     @task
#     def add_to_cart(self):
#         self.client.post("/api/cart", json={
#             "product_id": random.randint(1000, 2000),
#             "quantity": 1
#         })
#
#
# class PayUser(AuthenticatedUser):
#     user_type = "pay"
#
#     @task
#     def make_payment(self):
#         self.client.post("/api/pay", json={
#             "order_id": random.randint(5000, 6000),
#             "method": "credit"
#         })
from locust import HttpUser, task, between, TaskSet
from queue import LifoQueue

token=LifoQueue()

class longin_test(TaskSet):

    #只做登录
    @task(1)
    def do_login(self):
        subtype="logign"
        path="/webApi/login"
        rep=self.client.get(url=path,params={"phoneNum":18665868717,"pass":111111},name="登录").json()
        token.put(rep["data"]["token"])
        print(rep["data"]["token"])


    @task(1)
    def on_cat_devices(self):
        try:
            token_value = token.get_nowait() # 非阻塞方式获取 token
            print(f"Token: {token_value}")
            path = "/device/findByUserId"
            rep = self.client.post(url=path, data={"token": token_value}, name="查看设备").json()
            print(rep)
        except :
            print("没有 token")


class User_test(HttpUser):
    tasks = [longin_test]
    host= "https://tuying.mncats365.com"
    wait_time = between(1, 2)

