import sys

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, qApp


class Window(QWidget):
    # self 是当前类的实例对象
    def __init__(self):
        super().__init__()
        print("xxx")
        self.setWindowTitle("Qobject学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.QObject_test()
        self.Qobject_name_property_operation()

    def QObject_test(self):
        # QObject.__subclasses__() #某个类下面的所有子类
        mros = QObject.mro()
        for mro in mros:
            print(mro)

    def Qobject_name_property_operation(self):
        # ********** **********开始
        # obj=QObject()
        # obj.setObjectName("设置名字")#给一个QT对象设置一个名称，名称唯一，当作对象ID来使用
        # print(obj.objectName()) #获取QT对象名称
        #
        # obj.setProperty("notice_","error")#给一个QT对象动态的添加一个属性与值
        # obj.setProperty("notice_1","warning")
        # print(obj.property("notice_")) #获取对象的属性值
        # print(obj.dynamicPropertyNames())#获取一个对象中所有通过setProperty（）设置的属性名字

        # ********** **********结束

        # **********案例演示**********开始
        with open("QObject.qss", "r") as f:
            qApp.setStyleSheet(f.read())

        label = QLabel(self)
        label.setText("测试")
        label.setObjectName("notice")

        label = QLabel(self)
        label.setText("测试1")
        label.move(100,10)
        label.setObjectName("notice")
        label.setProperty("notice_level","normal")

        btn=QPushButton(self)
        btn.setText("按钮")
        btn.move(200,50)
        btn.setObjectName("butyt1")
        # label.setStyleSheet("font-size: 20px; color: red")
        # **********案例演示**********结束


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
