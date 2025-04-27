import sys

from PyQt5.Qt import *
from PyQt5.uic.Compiler.qtproxies import QtGui, QtCore


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("事件消息学习")
        self.resize(500,500)
        self.setup_ui()
        # self.setMouseTracking(True)

    def setup_ui(self):
        pass

    def showEvent(self,Event):
        print("窗口被显示了",Event)

    def closeEvent(self,Event):
        print("窗口被关闭了",Event)

    def moveEvent(self, a0: QtGui.QMoveEvent) -> None:
        print("窗口被移动了",a0)

    def resizeEvent(self, a0: QtCore.QSize) -> None:
        print("窗口调整了大小",a0)

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        print("鼠标进入时触发")
        self.setStyleSheet("background-color: yellow;")

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        print("鼠标离开时触发")
        self.setStyleSheet("background-color: red")
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("鼠标按下时触发",a0)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("鼠标释放触发")

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("鼠标双击时触发")

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("鼠标按下后移动触发")

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        print("有键盘被按住了")

    def  keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        print("键盘被按住后释放调用",a0)

    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None:
        print("获取焦点了")

    def focusOutEvent(self, a0: QtGui.QFocusEvent) -> None:
        print("失去了焦点")

    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None:
        print("拖拽进入控件时调用")
    def dragLeaveEvent(self, a0: QtGui.QDragLeaveEvent) -> None:
        print("拖拽离开空间时调用")
    def dragMoveEvent(self, a0: QtGui.QDragMoveEvent) -> None:
        print("拖拽在控件内移动时调用")
    def dropEvent(self, a0: QtGui.QDropEvent) -> None:
        print("拖拽放下时调用")

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        print("显示控件，更新控件时调用")

    def changeEvent(self, a0: QtCore.QEvent) -> None:
        print("窗体改变，字体改变时调用")

    def contextMenuEvent(self, a0: QtGui.QContextMenuEvent) -> None:
        print("访问右键菜单时调用")
if __name__ == '__main__':
    app =QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec())