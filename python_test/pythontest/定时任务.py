# from datetime import datetime
# from threading import Timer


# def pr_shei():
#     print("定时任务")
# def task():
#     now = datetime.now()
#     ts = now.strftime("%Y-%m-%d %H:%M:%S")
#     print(ts)
#
#
# def func():
#     pr_shei()
#     t = Timer(3, func)
#     t.start()
#
#
# func()


from timeloop import Timeloop
from datetime import timedelta
# tl = Timeloop()
# @tl.job(interval=timedelta(seconds=2))
# def sample_job_every_2s():
#     print ("2s job current time : {}".format(time.ctime()))
# @tl.job(interval=timedelta(seconds=5))
# def sample_job_every_5s():
#     print ("5s job current time : {}".format(time.ctime()))
# @tl.job(interval=timedelta(seconds=10))
# def sample_job_every_10s():
#     print ("10s job current time : {}".format(time.ctime()))
#
#





#
# from tkinter import *
# import threading
# import time
#
# # 创建主窗口
# root = Tk()
# # 设置窗口标题
# root.title("Canvas")
# # 创建Canvas对象
# canvas = Canvas(root, width=200, height=200)
# list=[]
# # 定义函数来更新Canvas画布
# def update_canvas():
#     for i in list:
#         # 移动矩形
#         canvas.move(i, 10, 0)
#     # 重新绘制Canvas
#     canvas.update()
#     # 每隔1秒钟调用一次update_canvas函数
#     canvas.after(1000, update_canvas)
# # 显示Canvas对象
# canvas.pack()
# # 调用update_canvas函数开始刷新Canvas
# canvas.after(1000, update_canvas)
#
# def d():
#     rectangle_id = canvas.create_line(10,10,10,100)
#     list.append(rectangle_id)
#     print(rectangle_id,type(rectangle_id))
#     time.sleep(1)
#     # canvas.update()
#     rectangle_id3 = canvas.create_line(0,0,0,0)
#     list.append(rectangle_id3)
#     print(rectangle_id3, type(rectangle_id3))
#     time.sleep(1)
#
#     rectangle_id2 = canvas.create_line(10,10,10,100)
#     list.append(rectangle_id2)
#     time.sleep(1)
#     # canvas.update()
#     print(rectangle_id2, type(rectangle_id2))
#
# # 进入消息循环
# thread=threading.Thread(target=d)
# thread.start()
# root.mainloop()


#
# from tkinter import *
# import threading
# import time
#
# # 创建主窗口
# root = Tk()
# # 设置窗口标题
# root.title("Canvas")
# # 创建Canvas对象
# canvas = Canvas(root, width=200, height=200)
# list=[]
# # 定义函数来更新Canvas画布
# def update_canvas():
#     for i in list:
#         # 移动矩形
#         canvas.move(i, 10, 0)
#     # 重新绘制Canvas
#     canvas.update()
#     # 每隔1秒钟调用一次update_canvas函数
#     canvas.after(1000, update_canvas)
# # 显示Canvas对象
# canvas.pack()
# # 调用update_canvas函数开始刷新Canvas
# canvas.after(1000, update_canvas)
# def send_data():
#     pass
#
#
# def d():
#     rectangle_id = canvas.create_line(10,10,10,100)
#     list.append(rectangle_id)
#     print(rectangle_id,type(rectangle_id))
#     time.sleep(1)
#     # canvas.update()
#     rectangle_id3 = canvas.create_line(0,0,0,0)
#     list.append(rectangle_id3)
#     print(rectangle_id3, type(rectangle_id3))
#     time.sleep(1)
#
#     rectangle_id2 = canvas.create_line(10,10,10,100)
#     list.append(rectangle_id2)
#     time.sleep(1)
#     # canvas.update()
#     print(rectangle_id2, type(rectangle_id2))
#
# # 进入消息循环
# thread=threading.Thread(target=d)
# thread.start()
# root.mainloop()




import threading
import time

# 线程1要执行的任务
def func1():
    while True:
        print("Thread 1 is running \n")
        time.sleep(1)

# 线程2要执行的任务
def func2():
    print("Thread 2 is running")

# 创建线程1，并指定它要执行的任务为func1()
t1 = threading.Thread(target=func1)

# 创建线程2，并指定它要执行的任务为func2()
t2 = threading.Thread(target=func2)

# 启动线程1和线程2
t1.start()
t2.start()

# 主线程等待两个子线程结束
t1.join()
t2.join()