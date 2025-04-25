import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class NineGridDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("九宫格接口展示")
        self.resize(500, 300)
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # 假设这是你接口返回的数据，每项可能包括图片路径和文字
        data_list = self.fetch_data()

        self.render_grid(data_list)

    def fetch_data(self):
        # 模拟接口返回数据（你可以换成 requests 获取接口）
        return [
            {"img": "./WX20250424-115852.png", "text": "Item 1"},
            {"img": "./WX20250424-115852.png", "text": "Item 2"},
            {"img": "./WX20250424-115852.png", "text": "Item 3"},
            {"img": "./WX20250424-115852.png", "text": "Item 4"},
            {"img": "./WX20250424-115852.png", "text": "Item 5"},
            {"img": "./WX20250424-115852.png", "text": "Item 6"},
            {"img": "./WX20250424-115852.png", "text": "Item 7"},
        ]

    def render_grid(self, data_list):
        columns = 3
        for index, item in enumerate(data_list):
            r = index // columns
            c = index % columns

            box_layout = QVBoxLayout()
            box_layout.setContentsMargins(0, 0, 0, 0)
            box_layout.setSpacing(0)

            container = QWidget()
            container.setLayout(box_layout)
            container.setStyleSheet("""
                background-color: rgb(248,248,255);
                border: 1px solid #aaa;
                border-radius: 12px;
            """)

            # 图片部分
            img_label = QLabel()
            pixmap = QPixmap(item["img"])
            img_label.setPixmap(pixmap)
            img_label.setScaledContents(True)
            img_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            img_label.setFixedHeight(150)

            # 文字部分
            text_label = QLabel(item["text"])
            text_label.setFixedHeight(50)
            text_label.setAlignment(Qt.AlignCenter)
            text_label.setStyleSheet("background-color: rgb(220,220,220);")

            box_layout.addWidget(img_label)
            box_layout.addWidget(text_label)

            self.grid.addWidget(container, r, c)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NineGridDemo()
    window.show()
    sys.exit(app.exec_())
