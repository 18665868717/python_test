import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class my_jiugongge(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setup_ui()


    def setup_ui(self):
        grid= QGridLayout()
        self.setLayout(grid)
        # label=QLabel(self)
        # label.setText("第一个")
        # label.resize(100,100)
        # label.setStyleSheet("background-color: rgb(248,248,255);")
        # label1=QLabel(self)
        # label1.setText("第二个")
        # label1.resize(100,100)
        # label1.setStyleSheet("background-color: rgb(245,245,245);")
        # grid.addWidget(label1,0,0)
        # grid.addWidget(label,0,1)

        for c in range(3):
            for r in range(3):
                box_layou=QVBoxLayout()
                box_layou.setContentsMargins(0,0,0,0)
                box_layou.setSpacing(0)

                con_=QWidget()
                con_.setLayout(box_layou)
                con_.setStyleSheet("background-color: rgb(248,248,255);")
                #border-top-left-radius: 12px;border-top-right-radius: 12px;
                imgpath=r"./WX20250424-115852.png"
                label = QLabel()
                pixmap=QPixmap(imgpath)
                label.setPixmap(pixmap)
                label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                label.setScaledContents(True)

                # label.setText("图片")
                # label.setStyleSheet("background-color: rgb(240,248,255);")
                # label.setContentsMargins(0,0,0,0)

                label1=QLabel(str(r) + "+" + str(c))
                label1.setFixedHeight(70)
                label1.setStyleSheet("background-color: rgb(220,220,220);")
                label1.setContentsMargins(0,0,0,0)
                box_layou.addWidget(label)
                box_layou.addWidget(label1)
                # label.setText(str(r) + "+" + str(c))
                # label.resize(150,150)
                # label.setStyleSheet("background-color: rgb(248,248,255);")
                grid.addWidget(con_,r,c)
        print(0 // 3)
        print(1 // 3)
        print(2 // 3)
        print(3 // 3)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=my_jiugongge()
    win.show()
    sys.exit(app.exec())