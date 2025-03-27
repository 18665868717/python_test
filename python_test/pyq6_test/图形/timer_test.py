import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, pyqtSlot
class TimerExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个 QTimer 实例
        self.timer = QTimer(self)
        # 设置定时器间隔为 1000 毫秒（1 秒）
        self.timer.setInterval(1000)
        # 连接定时器超时的信号到 on_timeout 槽函数
        self.timer.timeout.connect(self.on_timeout)
        # 开始定时器
        # self.timer.start()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PyQt Timer Example')
        self.show()

    @pyqtSlot()
    def on_timeout(self):
        # 在这里编写定时任务
        print("Timer timeout!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimerExample()
    sys.exit(app.exec_())