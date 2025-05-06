import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

#1.创建一个应用程序对象
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=QWidget()


#2.1设置控件
window.setWindowTitle("窗口相关操作")
window.resize(500,500)
# window.setWindowIcon(QIcon(r"./img.png")) #设置窗口icon
# window.setBackgroundRole(50)
# window.setWindowOpacity(0.5) #设置透明度


# print(window.windowState() == Qt.WindowNoState)#获取窗口状态
window.setWindowState(Qt.WindowMinimized)#设置窗口最小化
window.setWindowState(Qt.WindowMaximized)#设置窗口最大化

#2.3展示控件
window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
