import sys
from ui.ui import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QPointF, QRect, QPoint, QObject
from PyQt5.QtGui import QPainter, QPixmap, QColor, QMouseEvent, QPolygon
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication

from utils import *
from geometric import Point
from constants import DrawConst


class MyWin(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # размеры холста (ширрина и высота) в пикселях
        self.width = self.ui.canvas.width()
        self.height = self.ui.canvas.height()

        self.o_x = int(self.width * DrawConst.centerX)
        self.o_y = int(self.height * DrawConst.centerY)

        self._init_canvas(self.width, self.height)

    def _init_canvas(self, w, h):
        """
        @breif Начальная инициализиция холста
        @param w: ширина холста
        @param h: высота холста
        """
        self.pixmap = QPixmap(w, h)
        self.pixmap.fill(Qt.white)
        painter = QPainter()
        painter.begin(self.pixmap)

        if DrawConst.axes:
            self.drawAxes(painter)
        if DrawConst.grid:
            self.drawGrid(painter)

        self.drawLine(painter, Point(0, 0), Point(10, 5))

        painter.end()

        self.setPixmap()

    def drawGrid(self, painter: QPainter):
        """
        Метод для рисования сетки
        :param: painter объект QPainter для рисования
        """
        for dx in range(0, self.width, DrawConst.scaleX):
            painter.drawLine(dx, 0, dx, self.height)

        for dy in range(0, self.height, DrawConst.scaleY):
            painter.drawLine(0, dy, self.width, dy)

    def drawAxes(self, painter: QPainter):
        """
        Метод для рисования осей с подписями
        :param: painter объект QPainter для рисования
        """
        painter.drawLine(0, self.o_y, self.width, self.o_y)
        painter.drawLine(self.o_x, 0, self.o_x, self.height)

        for dx in range(0, self.width, DrawConst.scaleX):
            if dx == self.o_x:
                continue
            painter.drawEllipse(QPoint(dx, self.o_y), 1, 1)
            qp: QPoint = QPoint(dx, self.o_y)
            painter.drawText(dx-2, self.o_y-2, str(int(self.to_decart(qp).x())))

        for dy in range(0, self.height, DrawConst.scaleY):
            if dy == self.o_y:
                continue
            painter.drawEllipse(QPoint(self.o_x, dy), 1, 1)
            qp: QPoint = QPoint(self.o_x, dy)
            painter.drawText(self.o_x+4, dy+4, str(int(self.to_decart(qp).y())))

    def drawLine(self, painter: QPainter, a: Point, b: Point):
        painter.drawLine(self.to_qpoint(a), self.to_qpoint(b))

    def setPixmap(self):
        """
        Установить pixmap на lable(холст)
        """
        self.ui.canvas.setPixmap(self.pixmap)

    def to_decart(self, qpoint: QPoint):
        """
        Преобразования точки в декартовы координаты
        :param: qpoint точка в координатах холста(пиксели)
        """
        x = (qpoint.x() - self.o_x) / DrawConst.scaleX
        y = (-qpoint.y() + self.o_y) / DrawConst.scaleY
        return Point(x, y)

    def to_qpoint(self, point: Point):
        """
        Преобразования точки в в координаты холста(пиксели)
        :param: point точка в декартовых координатах
        """
        x = point.x() * DrawConst.scaleX + self.o_x
        y = -point.y() * DrawConst.scaleY + self.o_y
        return QPoint(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())