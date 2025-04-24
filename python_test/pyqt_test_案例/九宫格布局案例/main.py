# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import Qt
#
# class ImageGrid(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("九宫格图片展示")
#         self.initUI()
#
#     def initUI(self):
#         grid_layout = QGridLayout()
#         self.setLayout(grid_layout)
#
#         # 假设你有 9 张图片
#         image_paths = [
#             "./WX20250424-115852.png", "./WX20250424-115852.png", "./WX20250424-115852.png",
#             "./WX20250424-115852.png", "./WX20250424-115852.png", "./WX20250424-115852.png",
#             "./WX20250424-115852.png", "./WX20250424-115852.png", "./WX20250424-115852.png"
#         ]
#
#         # 将图片添加到九宫格中
#         position = 0
#         for row in range(3):
#             for col in range(3):
#                 if position < len(image_paths):
#                     pixmap = QPixmap(image_paths[position])
#                     label = QLabel()
#                     label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
#                     label.setAlignment(Qt.AlignCenter)
#                     grid_layout.addWidget(label, row, col)
#                     position += 1
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = ImageGrid()
#     window.show()
#     sys.exit(app.exec_())



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageGrid(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("九宫格图片 + 文字描述")
        self.initUI()

    def initUI(self):
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        # 图片路径和对应的描述
        items = [
            ("./WX20250424-115852.png", "描述1"),
            ("./WX20250424-115852.png", "描述2"),
            ("./WX20250424-115852.png", "描述3"),
            ("./WX20250424-115852.png", "描述4"),
            ("./WX20250424-115852.png", "描述5"),
            ("./WX20250424-115852.png", "描述6"),
            ("./WX20250424-115852.png", "描述7"),
            ("./WX20250424-115852.png", "描述8"),
            ("./WX20250424-115852.png", "描述9"),
        ]

        position = 0
        for row in range(3):
            for col in range(3):
                if position < len(items):
                    img_path, text = items[position]

                    # 垂直布局：图片 + 描述
                    vbox = QVBoxLayout()
                    label_img = QLabel()
                    pixmap = QPixmap(img_path)
                    label_img.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                    label_img.setAlignment(Qt.AlignCenter)

                    label_text = QLabel(text)
                    label_text.setAlignment(Qt.AlignCenter)

                    vbox.addWidget(label_img)
                    vbox.addWidget(label_text)

                    # 包装成一个 widget 加入九宫格
                    container = QWidget()
                    container.setLayout(vbox)

                    grid_layout.addWidget(container, row, col)

                    position += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageGrid()
    window.show()
    sys.exit(app.exec_())
