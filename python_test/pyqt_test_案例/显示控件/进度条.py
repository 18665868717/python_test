import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer

class ProgressBarExample(QMainWindow):
    va = 0
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QProgressBar 示例")
        self.setGeometry(100, 100, 400, 200)

        # 创建主部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建 QProgressBar 控件
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)  # 设置进度条范围为 0 到 100
        self.progress_bar.setTextVisible(True)  # 显示文本
        self.progress_bar.setFormat("{value}%")  # 显示进度百分比

        # 创建按钮
        self.button = QPushButton("开始", self)
        self.button.clicked.connect(self.start_progress)

        # 将控件添加到布局
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.button)

        # 创建定时器
        self.timer = QTimer(self)
        self.progress_value = 0
        self.timer.timeout.connect(self.update_progress)


    def start_progress(self):
        self.progress_value = 0
        self.progress_bar.setValue(self.progress_value)  # 重置进度条
        self.timer.start(100)  # 每 100 毫秒更新一次进度条

    def update_progress(self):
        self.progress_value += 1
        self.progress_bar.setValue(self.progress_value)  # 更新进度条
        if self.progress_value == 100:
            self.timer.stop()  # 停止定时器

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProgressBarExample()
    window.show()
    sys.exit(app.exec_())