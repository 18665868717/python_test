import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc

from PyQt6.QtCore import Qt

import tabel_ui

class My_Books(qw.QMainWindow,tabel_ui.Ui_Form):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.setupUi(self)
        self.add_data()

    def add_data(self):
        book_list=[["1","辰东","完美世界","2","经典"],["12","辰东","遮天","1","经典"]]
        self.tableWidget.setRowCount(len(book_list))  # 设置行数

        for row, book in enumerate(book_list):
            for col, data in enumerate(book):
                item = qw.QTableWidgetItem(data)
                self.tableWidget.setItem(row, col, item)

if __name__ == '__main__':
    app=qw.QApplication(sys.argv)
    ui=My_Books()
    ui .show()
    sys.exit(app.exec())