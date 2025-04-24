import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('动态折线图')
        self.setGeometry(600, 600, 600, 600)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout(self.centralWidget)

        self.plot = pg.PlotWidget()
        layout.addWidget(self.plot)

        # self.data = np.random.normal(size=(100,))  # 初始化数据
        self.data = np.random.uniform(low=0, high=0, size=25)   # 初始化数据
        self.plotCurve = self.plot.plot(self.data, pen='r')  # 创建折线图

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updatePlot)
        self.timer.start(100)  # 每100毫秒更新一次图表

    def updatePlot(self):
        # newData = np.random.normal()  # 生成新的数据点
        newData = np.random.randint(0, 11)
        self.data = np.roll(self.data, -1)  # 将数据向左滚动一个位置
        self.data[-1] = newData  # 将新的数据点添加到末尾
        self.plotCurve.setData(self.data)  # 更新折线图的数据
        self.plot.replot()  # 重新绘制图表


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())