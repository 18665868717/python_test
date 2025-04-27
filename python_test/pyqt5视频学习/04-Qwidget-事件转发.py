import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.uic.Compiler.qtproxies import QtGui


class Window(QWidget):
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("顶层窗口鼠标被按下了")

class MidWindow(QWidget):
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("中间控件被按下")


class Label(QLabel):
    """子类没有处理事件会转发给父类
    button不会转发给父控件，button本身就是处理点击事件
    """
    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        print("标签控件被点击")
        # ev.accept() #已经处理不再转发给父类
        ev.ignore() #继续向上转发


#1.创建一个应用程序对象
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=Window()


#2.1设置控件
window.setWindowTitle("事件转发")
window.resize(500,500)

mid=MidWindow(window)
mid.resize(400,400)
mid.setAttribute(Qt.WA_StyledBackground,True)
mid.setStyleSheet("background-color: red")


lab=Label(mid)
lab.setText("标签")
lab.setStyleSheet("background-color: yellow")
lab.move(100,100)

#2.3展示控件
window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
