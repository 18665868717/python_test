from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class TreeDemo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("三级导航示例")
        self.resize(400, 300)

        layout = QtWidgets.QVBoxLayout(self)

        self.tree = QtWidgets.QTreeWidget()
        self.tree.setHeaderHidden(True)  # 不显示表头

        # 添加顶层分类
        root1 = QtWidgets.QTreeWidgetItem(self.tree)
        root1.setText(0, "图书分类")

        # 二级分类
        literature = QtWidgets.QTreeWidgetItem(root1)
        literature.setText(0, "文学")

        tech = QtWidgets.QTreeWidgetItem(root1)
        tech.setText(0, "科技")

        # 三级子分类
        QtWidgets.QTreeWidgetItem(literature).setText(0, "古典")
        QtWidgets.QTreeWidgetItem(literature).setText(0, "当代")

        QtWidgets.QTreeWidgetItem(tech).setText(0, "计算机")
        QtWidgets.QTreeWidgetItem(tech).setText(0, "通信")

        self.tree.expandAll()  # 默认展开所有项

        layout.addWidget(self.tree)

        # 可选：绑定点击事件
        self.tree.itemClicked.connect(self.on_item_clicked)

    def on_item_clicked(self, item, column):
        print("你点击了：", item.text(0))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    demo = TreeDemo()
    demo.show()
    sys.exit(app.exec())
