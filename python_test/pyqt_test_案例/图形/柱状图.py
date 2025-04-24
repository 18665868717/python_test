# import sys
# from PyQt5 import QtWidgets
# import pyqtgraph as pg
# import numpy as np
#
# # 创建应用程序和窗口
# app = QtWidgets.QApplication(sys.argv)
# w = QtWidgets.QMainWindow()
# cw = QtWidgets.QWidget()
# w.setCentralWidget(cw)
# l = QtWidgets.QVBoxLayout()
# cw.setLayout(l)
#
# # 创建一个Bar图表对象
# bw = pg.BarGraphItem(x=np.array([1,2,3,4,5,6,7,8,9,10]), height=np.array([10,15,20,10,5,0,0,8,4,10]), width=0.3)
#
# # 创建GraphicsLayoutWidget容器，并加入到窗口中
# gw = pg.GraphicsLayoutWidget()
# l.addWidget(gw)
#
# # 创建一个PlotItem对象
# pw = gw.addPlot()
# pw.addItem(bw)
#
# w.show()
#
# if __name__ == '__main__':
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore
import pyqtgraph as pg
import numpy as np

# 这是主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 初始化数据
        self.x = np.array(list(range(1,11)))  # X轴数据
        print(self.x)
        self.y = np.array([0] * 10)         # Y轴数据（初始为0）

        # 创建一个图形项
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')

        self.setCentralWidget(self.graphWidget)

        # 创建柱状图项目
        self.bargraph = pg.BarGraphItem(x=self.x, height=self.y, width=0.3,pen=(218, 112, 214))
        axis = pg.AxisItem(orientation='bottom')  # 创建X轴的AxisItem对象
        axis.setTickSpacing(1, 10)  # 设置刻度间隔为1
        # axis.setTickOffset(0)  # 设置刻度偏移为0
        axis.setPen(pg.mkPen(color=(218, 112, 214)))

        self.graphWidget.addItem(self.bargraph)

        # 设置更新计时器
        self.timer = QTimer()
        self.timer.setInterval(500)  # 设置计时器间隔（1秒）
        self.timer.timeout.connect(self.update_plot)  # 连接更新函数
        self.timer.start()  # 启动计时器

    def update_plot(self):
        # 更新数据
        self.y = np.roll(self.y, -1)  # 左移动一个位置
        self.y[-1] = np.random.randint(0, 10)  # 随机生成一个新的数据

        # 更新柱状图，这里的x=self.x可以省略，因为x值没有变化
        self.bargraph.setOpts(height=self.y)

# 创建Qt应用程序和窗口
app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())