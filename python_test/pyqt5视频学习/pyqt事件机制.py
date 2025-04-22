import sys
from PyQt5.Qt import *


class App(QApplication):
    def notify(self, recevier, evt) :
        if recevier.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
            print(recevier, evt)

        return super().notify(recevier,evt)
class But(QPushButton):
    def event(self, evt):
        print("按钮被点击了---")
        return  super().event(evt)

app= App(sys.argv)
window=QWidget()

but=QPushButton(window)
but.setText("anniu")
but.move(100,100)

def cao():
    print("bei dianjile ")
but.pressed.connect(cao)

window.show()

sys.exit(app.exec())