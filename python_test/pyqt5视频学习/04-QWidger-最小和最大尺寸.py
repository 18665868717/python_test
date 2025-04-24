import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

#1.创建一个应用程序对象
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=QWidget()


#2.1设置控件
window.setWindowTitle("最大和最小尺寸")
# window.resize(500,500)
# window.setFixedSize(500,500)
# window.setMinimumSize(200,200)
# window.setMaximumSize(500,500)
window.setMinimumWidth(200)
window.setMinimumHeight(200)

window.setMaximumWidth(600)
window.setMaximumHeight(600)

#2.3展示控件
window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
