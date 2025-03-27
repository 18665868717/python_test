import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc

import pyqt_com


class mymainwindow(qw.QMainWindow, pyqt_com.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 加载配置文件以及编码格式
        self.settings=qc.QSettings("config.ini", qc.QSettings.IniFormat)
        self.settings.setIniCodec("UTF-8")
        # 获取配置信息
        # self.config_uart_baud=self.settings.value("UART_BAUD")
        # print("self.config_uart_baud的类型是",type(self.config_uart_baud))
        self.config_uart_baud1=self.settings.value("UART_BAUD",0,type=int)

        self.comboBox_btl.setCurrentText(str(self.config_uart_baud1))
        # self.comboBox_btl.setCurrentText(self.config_uart_baud1)

        # self.pushButton.clicked(self.pushButton_cb)
        self.pushButton.clicked.connect(self.pushButton_cb)

    def comboBox_btl_cd(self):
        print("出发了")
        btl_txt=self.comboBox_btl.currentText()
        qw.QMessageBox.information(self,"提示","当前选择的是:%s" %btl_txt,qw.QMessageBox.Ok|qw.QMessageBox.Cancel)
    def pushButton_cb(self):
        btl_tx=self.comboBox_btl.currentText()
        self.settings.setValue("UART_BAUD",btl_tx)
        print(btl_tx)




if __name__ == '__main__':
    app=qw.QApplication(sys.argv)
    w=mymainwindow()
    # w=qw.QMainWindow()
    # ui=pyqt_com.Ui_MainWindow()
    # ui.setupUi(w)
    w.show()

    sys.exit(app.exec())