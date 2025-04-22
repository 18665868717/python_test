import sys

from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

txt= 10
vua=0

class My_object(QObject):
    def timerEvent(self, evt):
        print(evt,"1")
class My_Qlabel(QLabel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setText("10")
        self.move(100,100)
        self.setStyleSheet("color: red")
    def set_my_timer(self,s):
        self.timer_id = self.startTimer(s)
    def timerEvent(self,*args,**kwargs):
        print("xxx")
        value=int(self.text())
        value-=1
        self.setText(str(value))

        if value ==0:
            print("停止")
            self.killTimer(self.timer_id)
    def set_va(self,va):
        self.setText(va)
#1.创建一个应用程序对象
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=QWidget()


#2.1设置控件
window.setWindowTitle("定时器的使用")
window.resize(500,500)

label= My_Qlabel(window)
label.set_va("99")
label.set_my_timer(5000)

label2= My_Qlabel(window)
label2.set_va("99")
label2.set_my_timer(1000)
label2.move(20,20)

#2.3展示控件
window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
