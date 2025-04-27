import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.uic.Compiler.qtproxies import QtCore

# class Window(QWidget):
#     pass
class my_label(QLabel):

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.setText("欢迎光临")

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.setText("谢谢回顾")

#1.创建一个应用程序对象
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=QWidget()


#2.1设置控件
window.setWindowTitle("")
window.resize(500,500)

label=my_label(window)
label.move(100,100)
label.resize(60,20)
label.setText("11")

#2.3展示控件
window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
