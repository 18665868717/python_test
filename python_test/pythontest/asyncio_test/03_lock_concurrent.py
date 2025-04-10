import threading
import time

lock = threading.Lock()
class Account:
    def __init__(self, balance):
        self.balance = balance

def draw(accout, amount):
    with lock:
        if accout.balance >= amount:
            time.sleep(0.1)
            print(threading.current_thread().name, "取钱成功")
            accout.balance -= amount
            print(threading.current_thread().name, "余额：", accout.balance)
        else:
            print(threading.current_thread().name, "失败，余额不足")

if __name__ == '__main__':
    accout = Account(1000)
    aa = threading.Thread(name="aa", target=draw, args=(accout, 800))
    bb = threading.Thread(name="bb", target=draw, args=(accout, 800))
    aa.start()
    bb.start()
