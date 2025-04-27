import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.move_flag = False
        self.setWindowTitle("窗口移动学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel(self)
        label1.setText("标签")
        label1.setStyleSheet("background-color: yellow")
        label1.move(100, 100)

    def mousePressEvent(self, a0) -> None:
        self.move_flag =True
        self.mouse_x=a0.globalX()
        self.mouse_y=a0.globalY()
        print("鼠标按下",self.mouse_y,self.mouse_x)
        self.origin_x = self.x()
        self.origin_y = self.y()




    def mouseMoveEvent(self, a0) -> None:
        if self.move_flag:
            print("鼠标按下移动")
            move_x = a0.globalX()- self.mouse_x
            move_y = a0.globalY() -self.mouse_y
            print("鼠标的向量",move_x,move_y)
            dest_x =self.origin_x +move_x
            dest_y =self.origin_y +move_y
            self.move(dest_x,dest_y)

    def mouseReleaseEvent(self, a0) -> None:
        print("鼠标释放")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 2.1创建控件
    window = Window()

    # 2.1设置控件
    window.setWindowTitle("")
    window.resize(500, 500)
    window.setMouseTracking(True)
    # 1.创建一个应用程序对象

    # 2.控件的操作


    # 2.3展示控件
    window.show()
    # 3应用程序的执行，进入消息循环
    sys.exit(app.exec())

