import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

#1.创建一个应用程序对象
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=QWidget()


#2.1设置控件
window.setWindowTitle("交互状态")
window.resize(500,500)


btn=QPushButton(window)
btn.setText("按钮")
btn.pressed.connect(lambda : print("被点击了"))
# btn.setEnabled(False)#设置是否可以点击、
# btn.setVisible(False) #设置不可见
btn.hide()#隐藏控件

if btn.isEnabled():
    print("可以点击")
else:
    print("不可以点击")

#2.3展示控件
window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
