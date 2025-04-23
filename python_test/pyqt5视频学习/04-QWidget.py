import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

#1.创建一个应用程序对象
app=QApplication(sys.argv)

#2.控件的操作
#2.1创建控件
window=QWidget()

"""
move(x,y)
resize(width,height)
setGeometry(x,y,width,height)
adjustSize()  根据自适应大小
setFixedSize(x，y) 设置固定大小
"""
#2.1设置控件
window.move(200,100) #移动桌面左上100，100
# window.resize(500,500)
window.setFixedSize(500,500)  #固定大小，不能放大和缩小
# window.setGeometry(0,0,200,200)#用户区域，不包含标题栏


label = QLabel(window)
label.setText("文本")
label.move(100,100)
label.setStyleSheet("background-color: cyan;")
def changecao():
    new_content=label.text()+ "文本"
    label.setText(new_content)
    label.resize(label.width()+100,label.height())

but = QPushButton(window)
but.setText("anniu")
but.move(100,300)
but.clicked.connect(changecao)

#2.3展示控件
window.show()
#3应用程序的执行，进入消息循环
sys.exit(app.exec())
