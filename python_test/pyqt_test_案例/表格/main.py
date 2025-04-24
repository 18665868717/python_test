import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc

import tabel_ui

class My_Books(qw.QMainWindow,tabel_ui.Ui_Form):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.setupUi(self)
        self.add_data()

    def add_data(self):
        book_list=[["1","辰东","完美世界","2","经典"],["12","辰东","遮天","1","经典"]]
        self.tableWidget.setRowCount(len(book_list))  # 设置行数
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏行头
        self.tableWidget.setAlternatingRowColors(True) #间隔一行换个颜色

        # self.tableWidget.resizeColumnsToContents #自适应宽度
        self.tableWidget.setColumnWidth(0, 50)  # ID
        self.tableWidget.setColumnWidth(1, 120)  # 作者
        self.tableWidget.setColumnWidth(2, 200)  # 书名
        self.tableWidget.setColumnWidth(3, 80)  # 剩余数
        self.tableWidget.setColumnWidth(4, 200)  # 评论

        for row, book in enumerate(book_list):
            print("第一次遍历",row,book)
            for col, data in enumerate(book):
                print("第二次遍历",col,data)
                item = qw.QTableWidgetItem(data)
                item.setTextAlignment(qc.Qt.AlignCenter)
                self.tableWidget.setItem(row, col, item)

if __name__ == '__main__':
    app=qw.QApplication(sys.argv)
    ui=My_Books()
    ui .show()
    sys.exit(app.exec())