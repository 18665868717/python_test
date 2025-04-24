import sys

from PyQt5.QtWidgets import QWidget, QApplication

app =QApplication(sys.argv)

window=QWidget()
window.show()
window.resize(600,600)
window.move(300,300)


#总控件的个数
widget_count= 9
#一行有多少控件
column_count = 3
#计算一个控件的宽度
widget_width = int(window.width() / column_count)
#总共有多少行 （编号 // 一行多少列 + 1）
row_count=(widget_count - 1) // column_count + 1
widget_height = int(window.height() / row_count)

for i in range(0,widget_count):
    w=QWidget(window)
    w.resize(widget_width , widget_height)
    widget_x = i % column_count * widget_width
    widget_y = i // column_count * widget_height
    w.move(widget_x,widget_y)
    w.setStyleSheet("background-color: gray;border: 10px solid white;")
    w.show()

sys.exit(app.exec())