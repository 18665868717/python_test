
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedLayout, QPushButton

class StackableWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建主窗口
        self.setWindowTitle("Stacked Layout Example")
        self.setGeometry(100, 100, 400, 300)

        # 创建QStackedLayout
        self.stack_layout = QStackedLayout()

        # 创建两个子窗口（子部件）
        widget1 = QWidget()
        widget2 = QWidget()

        # 创建各自的布局
        layout1 = QVBoxLayout(widget1)
        layout2 = QVBoxLayout(widget2)

        # 添加子部件到各自的布局
        button1 = QPushButton("Switch to Widget 2", widget1)
        button2 = QPushButton("Switch to Widget 1", widget2)

        layout1.addWidget(button1)
        layout2.addWidget(button2)

        # 将布局添加到子部件
        widget1.setLayout(layout1)
        widget2.setLayout(layout2)

        # 将子部件添加到堆叠布局
        self.stack_layout.addWidget(widget1)
        self.stack_layout.addWidget(widget2)

        # 设置堆叠布局为中央部件
        central_widget = QWidget(self)
        central_widget.setLayout(self.stack_layout)
        self.setCentralWidget(central_widget)

        # 当按钮被点击时，切换栈顶
        button1.clicked.connect(lambda: self.stack_layout.setCurrentIndex(1))
        button2.clicked.connect(lambda: self.stack_layout.setCurrentIndex(0))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = StackableWindow()
    main_window.show()
    sys.exit(app.exec_())