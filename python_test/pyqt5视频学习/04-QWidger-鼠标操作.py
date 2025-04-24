import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class my_sbyidong(QWidget):
    def mouseMoveEvent(self, Event):
        print("鼠标按下去移动了",Event.localPos())
        label = self.findChild(QLabel)
        label.move(Event.x(),Event.y())

#1.创建一个应用程序对象
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=my_sbyidong()


#2.1设置控件
window.setWindowTitle("")
window.resize(500,500)
window.setMouseTracking(True) #鼠标跟踪
label=QLabel(window)
label.setText("111")
label.move(100,100)
print(window.hasMouseTracking())

"""
# window.setCursor(Qt.ArrowCursor) #默认
# window.setCursor(Qt.UpArrowCursor) #上箭头
pixmap = QPixmap("./img.png")
new_pixmap_=pixmap.scaled(20,20)#缩放
cousor = QCursor(new_pixmap_,0,0) #调聚焦点
window.setCursor(cousor) #十箭头

# window.unsetCursor()#恢复

current_cursor=window.cursor()
current_cursor.setPos(20,20) #鼠标移动屏幕20，20
"""


#2.3展示控件
window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
