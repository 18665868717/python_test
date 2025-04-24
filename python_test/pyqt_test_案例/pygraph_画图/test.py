# # import numpy as np
# # y = np.random.rand(10)
# # print(y)
#
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import numpy as np
# import time
#
# # 初始化数据
# data = np.random.randint(0, 100, size=10)  # 初始数据列表
# print("初始化数据列表",data)
# x = np.arange(len(data))  # X轴刻度
# print("X轴刻度标",x)
# fig, ax = plt.subplots()
# bars = ax.bar(x, data)
# ax.set_xticks(np.arange(0, len(data), 1))
# ax.set_yticks(np.arange(0, 101, 10))
#
# # 更新函数
# def update(frame):
#     global data
#     data = data[1:]  # 移除第一个元素
#     data = np.append(data, np.random.randint(0, 100))  # 添加新的随机值
#     print("现在的data值是",data)
#     for bar, h in zip(bars, data):
#         print("遍历的bar和h的值是",bar ,"--",h)
#         bar.set_height(h)
#     ax.set_xlim(0, len(data))  # 更新X轴范围
#     fig.canvas.draw()  # 重新绘制图形
#
# # 每秒更新一次
# ani = FuncAnimation(fig, update, interval=1000)
#
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

print(group_data)
print(group_names)
print(group_mean)
fig, ax = plt.subplots()
ax.barh(group_names,group_data)
plt.show()