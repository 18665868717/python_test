import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class Window(QWidget):
    #self 是当前类的实例对象
    def __init__(self):
        super().__init__()
        print("xxx")
        self.setWindowTitle("学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label=QLabel(self)
        label.setText("jij ")
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec())