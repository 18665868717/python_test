import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QKeyEvent


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab 键监听示例")
        self.resize(500, 500)

        # 创建标签
        self.label = QLabel("按下 Tab 键会更改文本", self)
        self.label.move(100, 100)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        # 监听 Tab 键按下
        if event.key() == Qt.Key_Tab:
            self.label.setText("Tab 键被按下了")
        else:
            super().keyPressEvent(event)  # 如果不是 Tab 键，则继续事件的默认处理


# 1. 创建应用程序对象
app = QApplication(sys.argv)

# 2. 创建并展示主窗口
window = MyWindow()
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec_())
