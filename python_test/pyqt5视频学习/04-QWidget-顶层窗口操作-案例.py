from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()

# 2.1 设置控件
window.setWindowTitle("顶层窗口操作-案例")
window.resize(500, 500)
window.setWindowFlags(Qt.FramelessWindowHint)  # 设置无边框窗口
window.setWindowOpacity(0.5)

close_but=QPushButton(window)
close_but.setText("关闭")

close_but_w =close_but.width()
window_w=window.width()

close_but_x =  window_w -close_but_w
close_but_y = 10
close_but.move(close_but_x,close_but_y)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入消息循环
sys.exit(app.exec())
