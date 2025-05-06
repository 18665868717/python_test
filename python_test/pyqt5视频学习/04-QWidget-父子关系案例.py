import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

# class Label(QLabel):
#     def mousePressEvent(self, ev) -> None:
#         self.setStyleSheet("background-color: red")
"""
要求：点击那个标签就让当前的标签变颜色，使用控件的方式操作
"""

class Windows(QWidget):

    def mousePressEvent(self, a0) -> None:
        print("111")
        local_X=a0.x()
        local_Y=a0.y()
        sub_widget=self.childAt(local_X,local_Y)
        if sub_widget:
            sub_widget.setStyleSheet("background-color: red")
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=Windows()


#2.1设置控件
window.setWindowTitle("父子关系案例")
window.resize(500,500)

for i in range(1,11):
    label=QLabel(window)
    label.setText("标签" +str(i))
    label.move(i*30,i*30)


#2.3展示控件
window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
