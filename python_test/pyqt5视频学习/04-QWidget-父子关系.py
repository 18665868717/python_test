import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

#1.创建一个应用程序对象
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=QWidget()


#2.1设置控件
window.setWindowTitle("父子关系的学习")
window.resize(500,500)
label= QLabel(window)
label.setText("标签1")



label2= QLabel(window)
label2.setText("标签2")
label2.move(50,50)

label3= QLabel(window)
label3.setText("标签3")
label3.move(100,100)
"""
childAt:获取指定坐标的控件
parentWidget()：获取指控件的父控件
childrenRect():所有子控件组成的边界矩形
"""
print(window.childAt(50, 50))
print(label3.parentWidget())
print(window.childrenRect())
#2.3展示控件
window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
