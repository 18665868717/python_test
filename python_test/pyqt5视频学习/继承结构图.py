import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from menu import Window


#1.创建一个应用程序对象
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=Window()


#2.1设置控件

#2.3展示控件
window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
