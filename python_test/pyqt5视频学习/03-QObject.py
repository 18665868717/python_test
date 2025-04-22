import sys

from PyQt5.QtCore import QObject, Qt
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
        # self.Qobject_name_property_operation()
        # self.QObjeck对象父子关系操作()
        # self.QWidget控件的信号操作()
        # self.QObject类型判断()
        self.QObject对象删除()
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

    def QObjeck对象父子关系操作(self):
        pass
        # **********测试API**********开始
        # obj1=QObject()
        # obj2=QObject()
        # obj3=QObject()
        # obj3.setObjectName("3")

        # print("obj1",obj1)
        # print("obj2",obj2)
        #
        # obj1.setParent(obj2) #将obj2设置为obj1父对象
        # obj3.setParent(obj2) #将obj2设置为obj1父对象
        # print(obj1.parent()) #获取父对象


        """ 参数1：子对象|参数2：子对象名字|递归查找"""
        # print(obj2.findChild(QObject,"3",Qt.FindDirectChildrenOnly))#获取子对象，只返回一个
        # print(obj2.findChild(QObject))#获取子对象，只返回一个



        # print("obj2的子对象",obj2.children())#获取obj2所有直接子对象

        # print(obj2.findChildren(QLabel))
        # **********测试API**********结束

    def QWidget控件的信号操作(self):
        # self.obj=QObject()
        # #bj.destroyed
        # #obj.objectNameChanged
        #
        # # def destroy_cao(obj):
        # #     print("对象被释放了",obj)
        # # self.obj.destroyed.connect(destroy_cao) #对象被释放的时候执行
        # # del self.obj
        #
        # def cangee_cao(name):
        #     print("对象名被修改了",name)
        # self.obj.objectNameChanged.connect(cangee_cao)
        # print(self.obj.receivers( self.obj.objectNameChanged))
        #
        # self.obj.setObjectName("bbb")
        # # print(self.obj.signalsBlocked(),1)
        # # self.objectNameChanged.disconnect()
        #
        # self.obj.setObjectName("aaa")
        #
        # # self.obj.objectNameChanged.connect(cangee_cao)
        # self.obj.blockSignals(True) #临时（取消）阻止指定控件所有的信号与槽的连接
        # # self.obj.blockSignals(False)
        # self.obj.setObjectName("aaabbb")
        # # print(self.obj.signalsBlocked(),2)

        # **********信号与槽案例**********开始
        def but_print():
            print("按钮被点击了")
        btn=QPushButton(self)
        btn.setText("按钮")
        btn.clicked.connect(but_print)

        # **********信号与槽案例**********结束

    def QObject类型判断(self):
        # """应用场景：过滤控件类型"""
        # # **********类型判断**********开始
        # obj = QObject()
        # w = QWidget()
        # btn = QPushButton()
        # bel = QLabel()
        #
        # objs = [obj, w, btn, bel]
        # for i in objs:
        #     # print(i.isWidgetType())遍历判断那些对象是QWidget
        #     print(i.inherits("QWidget"))  # 遍历判断那些对象继承QWidget
        # # **********类型判断**********结束



        # **********案例**********开始
        """
        obj.findChildren(QLabel) 指定查找某个类型的控件
        obj.children() 查找当前类下的所有控件

        """
        label1=QLabel(self)
        label1.setText("1111")

        label2=QLabel(self)
        label2.setText("2222")
        label2.move(100,0)

        but1=QPushButton(self)
        but1.setText("bt1")
        but1.move(100,100)

        # for i in findChildren(QLabel):
        for i in self.children():
            # if i.isWidgetType():
            if i.inherits("QLabel"):
                print(i,"是")
                i.setStyleSheet("color: red")
            else:
                i.setStyleSheet("color: yellow")

        # **********案例**********结束

    def QObject对象删除(self):
        obj1=QObject()
        obj2=QObject()
        obj3=QObject()
        self.obj1=obj1

        obj3.setParent(obj2)
        obj2.setParent(obj1)
        obj1.destroyed.connect(lambda :print("obj1被释放了"))
        obj2.destroyed.connect(lambda :print("obj2被释放了"))
        obj3.destroyed.connect(lambda :print("obj3被释放了"))

        obj2.deleteLater()#稍后删除,并解除关系
        print(obj1.children())

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = Window()
    win.show()

    # win1=QWidget()
    # win1.setStyleSheet("background-color: red")
    # win1.setWindowTitle("win1")
    # win1.show()
    #
    # win2=QWidget()
    # win2.setStyleSheet("background-color: green")
    # win2.setParent(win1)
    # win2.resize(100,100)
    # win2.show()

    """指定查找QLabel对象"""
    # win_root=QWidget()
    # label=QLabel(win_root)
    # label.setText("控件1")
    #
    # label2=QLabel(win_root)
    # label2.setText("控件2")
    # label2.move(100,100)
    #
    # label.setParent(win_root)
    # but=QPushButton(win_root)
    # but.setText("按钮")
    # but.move(200,200)
    # for i in win_root.findChildren(QLabel): #指定查找QLabel对象，并遍历
    #     i.setStyleSheet("color: green")
    #     # print(i)
    # win_root.show()

    sys.exit(app.exec())
