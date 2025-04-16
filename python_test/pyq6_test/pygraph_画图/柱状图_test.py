import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# # 初始化数据
# x = np.arange(15)
# print("第一步X",x)
# y = np.random.rand(15)
# print("第二步Y",y)
#
# fig, ax = plt.subplots()
# bars = ax.bar(x, y)
#
# def update_data(frame):
#     global y
#     y = np.roll(y, -1)  # 将数据向左滚动一位
#     y[-1] = np.random.rand()  # 用随机数替换最后一个数据
#     for bar, h in zip(bars, y):
#         bar.set_height(h)
#     return bars
#
# ani = animation.FuncAnimation(fig, update_data, interval=1000)
#
# plt.show()


# X_list=[0,0,0,0,0,0,0,0,0,0]
# Y_list=[0,10,20,30,40,50,60,70,80,90,100]
#
# fig, ax = plt.subplots()
# bars = ax.bar(X_list, Y_list)
#
# def update_data(frame):
#     global y
#     global Y_list
#     Y_list.pop()
#     Y_list.append(range(0,100))
#
#     for bar, h in zip(bars, Y_list):
#         bar.set_height(h)
#     return bars
#
# ani = animation.FuncAnimation(fig, update_data, interval=1000)
#
# plt.show()

import matplotlib.pyplot as plt
import matplotlib.animation as animation

X_list = [0,0,0,0,0,0,0,0,0,0]
Y_list = [0,10,20,30,40,50,60,70,80,90,100]

fig, ax = plt.subplots()
bars = ax.bar(X_list, Y_list)

def update_data(frame):
    global Y_list
    Y_list.pop(0)
    Y_list.append(frame)  # Assuming frame is a single value
    for bar, h in zip(bars, Y_list):
        bar.set_height(h)
    return bars

ani = animation.FuncAnimation(fig, update_data, frame=range(1, 100), interval=1000)

plt.show()
#使用matplotlib画柱状图，X轴刻度10，Y轴刻度100，然后每间隔1秒读取列表第一个值并实时显示，下一秒左移一个刻度并且再次读取列表的第一个值并实时显示