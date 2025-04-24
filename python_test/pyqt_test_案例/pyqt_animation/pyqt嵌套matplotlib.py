# -*- coding: utf-8 -*-
'''
python技巧之把animation的动态图嵌入pyqt5的界面中
'''

import sys
import numpy as np

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QLabel, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import QObject, Qt

import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import animation

n = 0


class App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle('就想有个标题')
        self.main_widget = QWidget(self)

        hBox = QHBoxLayout(self.main_widget)  # 横着布局
        vBox = QVBoxLayout(self.main_widget)  # 竖着布局

        self.canvas = Csi_plot(self.main_widget, width=5, height=4, dpi=100)
        vBox.addWidget(self.canvas)

        self.start_button = QPushButton('start', self)
        self.stop_button = QPushButton('stop', self)
        self.exit_button = QPushButton('exit', self)
        self.start_button.clicked.connect(self.on_start)
        self.stop_button.clicked.connect(self.on_stop)
        self.exit_button.clicked.connect(self.on_exit)
        hBox.addWidget(self.start_button)
        hBox.addWidget(self.stop_button)
        hBox.addWidget(self.exit_button)

        self.label = QLabel('<h1>?</h1>', self)
        # vBox.addWidget(self.label)
        self.label.setGeometry(0, 0, 120, 30)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_1 = QLabel('<h2>速度设置：</h2>', self)
        self.label_1.setGeometry(0, 50, 120, 30)
        self.linEdit = QLineEdit('2000', self)
        self.linEdit.setGeometry(90, 50, 120, 30)

        # 改变控件的颜色
        self.label.setAutoFillBackground(True)
        global palette_red, palette_green
        palette_red = QPalette()
        palette_green = QPalette()
        palette_red.setColor(QPalette.Window, Qt.red)
        palette_green.setColor(QPalette.Window, Qt.green)

        hBox.addLayout(vBox)
        self.setLayout(hBox)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        self.scat, = self.canvas.axes.plot([], [], lw=2)
        self.show()

    def update_function(self, i):
        global n
        if n % 2 == 0:
            x = np.linspace(0, 2, 1000)
            y = 5 * np.sin(10 * np.pi * (x - 0.01 * i))
            self.scat.set_color('r')
            self.label.setText('<h1>还是优秀也</h1>')
            self.label.setPalette(palette_red)
        else:
            x = np.linspace(-200, 200, 100)
            y = np.sin(2 * np.pi * (x - 0.01 * i))
            self.scat.set_color('b')
            self.label.setText('<h1>独秀</h1>')
            self.label.setPalette(palette_green)
        self.scat.set_data(x, y)
        n += 1
        return self.scat,
    def on_start(self):
        self.ani = animation.FuncAnimation(self.canvas.figure, self.update_function, frames=200,
                                           blit=True, interval=int(self.linEdit.text()))
    def on_stop(self):
        self.ani._stop()

    def on_exit(self):
        self.close()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Are you sure to exit?', QMessageBox.Yes | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
class Csi_plot(FigureCanvas):
    def __init__(self, parent=None, width=9, height=9, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.ax = fig.add_subplot(111)
        self.ax.set_xlim(0, 2)
        self.ax.set_ylim(-6, 6)
        self.ax.grid(True)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())