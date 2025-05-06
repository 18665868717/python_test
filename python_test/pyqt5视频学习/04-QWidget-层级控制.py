import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

#1.创建一个应用程序对象
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=QWidget()


#2.1设置控件
window.setWindowTitle("层级控制")
window.resize(500,500)
label=QLabel(window)
label.setText("标签1")
label.resize(100,100)
label.setStyleSheet("background-color: red")

label2=QLabel(window)
label2.setText("标签1")
label2.setStyleSheet("background-color: yellow")
label2.resize(100,100)

# label2.lower() #将控件降低到最底层
# label.raise_() #将控件降低到最上层
label2.stackUnder(label) #将2放在1下面
#2.3展示控件
window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
