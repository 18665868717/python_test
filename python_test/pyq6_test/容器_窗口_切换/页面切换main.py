import os
import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMainWindow
import PyQt5.QtWidgets as qw
import from_page_sw
class pages_window(from_page_sw.Ui_MainWindow,QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setupUi(self)

        self.pg_bt_1.clicked.connect(self.sw_page1)
        self.pg_bt_2.clicked.connect(self.sw_page2)
        self.pg_bt_3.clicked.connect(self.sw_page3)

    def sw_page1(self):

        self.stackedWidget.setCurrentIndex(2)
    def sw_page2(self):
        self.stackedWidget.setCurrentIndex(0)
    def sw_page3(self):
        self.stackedWidget.setCurrentIndex(1)
if __name__ == '__main__':
    app=qw.QApplication(sys.argv)
    w=pages_window()
    w.show()
    sys.exit(app.exec())