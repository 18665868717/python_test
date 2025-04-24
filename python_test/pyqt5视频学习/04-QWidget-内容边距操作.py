import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

#1.创建一个应用程序对象
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=QWidget()


#2.1设置控件
window.setWindowTitle("内容边距设置")
window.resize(500,500)
label= QLabel(window)


label.setText("该死的温柔")
label.resize(100,60)
label.setStyleSheet("background-color: red;")
label.setContentsMargins(10,10,10,10)#设置内容边距
window_width = window.width()
window_height = window.height()
label_width = label.width()
label_height = label.height()
label.move(window_width - label_width, window_height - label_height)

window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
