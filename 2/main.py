import sys
from ui.ui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
import random


class MyWin(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.draw)

    def DoIt(self):
        self.ui.label.setText(str(random.randint(1, 10)))

    def draw(self):
        width = self.ui.canvas.width()
        height = self.ui.canvas.height()
        pixmap = QPixmap(width, height)
        painter = QPainter()
        pixmap.fill(Qt.white)
        painter.begin(pixmap)

        painter.setBrush(QColor(200, 0, 0))
        painter.drawEllipse(0, 0, 500, 50)
        painter.drawPoint(10, 10)

        painter.end()
        self.ui.canvas.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
