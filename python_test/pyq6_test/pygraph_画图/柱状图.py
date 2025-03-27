import matplotlib.pyplot as plt
import numpy as np
import time
from collections import deque

# 设置初始的柱状图数据
data_length = 60  # X轴长度(数据点个数)
y_range = 100  # Y轴的最大值
data = deque(np.zeros(data_length), maxlen=data_length)  # 使用deque作为滑动窗口

# 创建画布和柱状图
plt.ion()  # 开启交互模式
fig, ax = plt.subplots()
bars = plt.bar(range(data_length), data)

# 更新柱状图的函数
def update_bars(data):
    for bar, h in zip(bars, data):
        bar.set_height(h)
    ax.relim()  # 重新计算坐标轴的限度
    ax.autoscale_view()  # 根据数据范围重新绘制坐标轴

# 主循环，每秒更新一次数据
try:
    while True:
        new_value = np.random.randint(0, y_range)  # 生成一个新的随机数据
        data.append(new_value)  # 添加到右侧，左侧的数据会被删除
        update_bars(data)  # 更新柱状图显示
        fig.canvas.draw()  # 重新绘制整个画布
        fig.canvas.flush_events()  # 刷新事件
        time.sleep(1)  # 等待一秒
except KeyboardInterrupt:
    plt.ioff()  # 关闭交互模式


plt.show()