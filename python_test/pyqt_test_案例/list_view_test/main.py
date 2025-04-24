
import sys
import PyQt5.QtWidgets as qw
import list_vi
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QStandardItemModel,QStandardItem
class mylistview(qw.QMainWindow,list_vi.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = QStringListModel([])
        self.listView_1.setModel(self.model)

        self.pushButton_add.clicked.connect(self.pushButton_add_cb)



    def pushButton_add_cb(self):
        line_edit_content=self.lineEdit.text()
        if len(line_edit_content)>0:
            data=self.model.stringList()
            data.append(line_edit_content)
            self.model.setStringList(data)
            self.lineEdit.clear()






if __name__ == '__main__':
    app=qw.QApplication(sys.argv)
    w=mylistview()

    w.show()
    sys.exit(app.exec())