import sys
import PyQt5.QtWidgets as qw
from PyQt5.QtCore import QTimer
import pyqt_graph
import pyqtgraph as pg
from PyQt5.QtWidgets import QVBoxLayout
import random


class mymain(qw.QMainWindow, pyqt_graph.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_but.clicked.connect(self.print_test)
        self.stop_but.clicked.connect(self.stop_animation)
        self.x = [0, 1, 2, 3, 4, 5, 6, 7, 8,]
        self.y = [0, 0, 0,0, 0, 0, 0, 0, 0,]
        self.animation_init()

    def print_test(self):
        print("tes")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updatePlot)
        self.timer.start(1000)  #

    def stop_animation(self):
        self.timer.stop()


    def animation_init(self):
        self.plot_widget.setMouseEnabled(x=False,y=False)

        # 在 Pyqtgraph 组件中绘制折线图

        self.bj1=pg.BarGraphItem(x=self.x,height=self.y,width=0.5,brush='r')
        self.plot_widget.addItem(self.bj1)
        self.plot_widget.resize(600,300)
        self.plot_widget.setXRange(0,8)
        self.plot_widget.setYRange(0,10)
        # self.plot_widget.plot(x, y, pen=pg.mkPen(color='b', width=2))  # 绘制蓝色的折线图


        # 将 Pyqtgraph 组件添加到 QGraphicsScene 中
        self.scene.addWidget(self.plot_widget)
        # 将 QGraphicsView 添加到主窗口中
        layout = QVBoxLayout()
        layout.addWidget(self.graphicsView)


    def updatePlot(self,):
        print("Y轴是：", self.y, )
        self.bj1.setOpts(x=self.x,height=self.y)

        del self.y[0]
        y_vl= random.randint(0, 10)
        self.y.append(y_vl)
        # print(self.y)

        # newData = np.random.normal()  # 生成新的数据点
        # newData = np.random.randint(0, 11)
        # self.data = np.roll(self.data, -1)  # 将数据向左滚动一个位置
        # self.data[-1] = newData  # 将新的数据点添加到末尾
        # self.plotCurve.setData(self.data)  # 更新折线图的数据
        # self.plot.replot()  # 重新绘制图表


if __name__ == '__main__':
    # app=qw.QApplication(sys.argv)
    # w=qw.QMainWindow()
    # ui=pyqt_graph.Ui_MainWindow()
    # ui.setupUi(w)
    # w.show()
    # sys.exit(app.exec())
    app=qw.QApplication(sys.argv)
    w=mymain()
    # w=qw.QMainWindow()
    # ui=pyqt_com.Ui_MainWindow()
    # ui.setupUi(w)
    w.show()

    sys.exit(app.exec())