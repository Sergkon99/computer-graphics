import sys
from ui.ui import *
from PyQt5.QtCore import Qt, QPointF, QRect, QPoint
from PyQt5.QtGui import QPainter, QPixmap, QColor, QMouseEvent
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
# from PyQt5.QtCore.QEvent import QMouseEvent
import random
from utils import Point, log_method
from constants import DrawConst
from typing import List


class MyWin(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # TODO это нужно вынести в константы
        r = 3
        self.figure = list(map(Point, [(-r, 0), (0, r), (r, 0), (0, -r)]))
        print(self.figure)

        # размеры холста (ширрина и высота) в пикселях
        self.width = self.ui.canvas.width()
        self.height = self.ui.canvas.height()
        # print(f'width={self.width}\nheight={self.height}')

        # координаты центра(0, 0) в координатах холста(в пикселях)
        self.o_x = self.width * DrawConst.centerX
        self.o_y = self.height * DrawConst.centerY

        # инициализируем холст
        self.__init_canvas(self.width, self.height)

        # связываем клик с вызовом функции
        self.ui.pushButton.clicked.connect(self.drawFigure)
        # self.drawFigure()


    def __init_canvas(self, w, h):
        """
        @breif Начальная инициализиция холста
        @param w: ширина холста
        @param h: высота холста
        """
        self.pixmap = QPixmap(w, h)
        self.pixmap.fill(Qt.white)
        painter = QPainter()
        painter.begin(self.pixmap)

        if DrawConst.grid:
            self.drawGrid(painter)

        painter.end()

        self.ui.canvas.setPixmap(self.pixmap)

    def DoIt(self):
        self.ui.label.setText(str(random.randint(1, 10)))

    @log_method
    def drawFigure(self, event=None):
        """
        @breif Основной метод для рисования фигуры
        @param event: без него не работает декоратор, возможно про срабатывании события что-то передаются
        """
        painter = QPainter()
        painter.begin(self.pixmap)

        if DrawConst.grid:
            self.drawGrid(painter)

        painter.setPen(Qt.red)
        self.drawEllipse(painter, self.figure)
        self.drawLine(painter, self.figure[0], self.figure[2])
        self.drawLine(painter, self.figure[1], self.figure[3])

        painter.end()
        self.ui.canvas.setPixmap(self.pixmap)

    @log_method
    def drawLine(self, painter: QPainter, p1: Point, p2: Point):
        """
        @breif Метод для рисования отрезка между точками
        @param painter: объект QPainter для рисования
        @param p1, p2: точки в декартовых координатах
        """
        p1 = self.to_qpoint(p1)
        p2 = self.to_qpoint(p2)
        painter.drawLine(p1, p2)

    @log_method
    def drawEllipse(self, painter: QPainter, points: List[Point]):
        """
        @breif Метод для рисования эллипса внтру прямоугольника
        @param painter: объект QPainter для рисования
        @param points: список точек в декартовых координатах, задающих прямоугольник
        """
        lu: Point = Point(min([p.x() for p in points]),
                          max([p.y() for p in points]))
        rd: Point = Point(max([p.x() for p in points]),
                          min([p.y() for p in points]))
        rect: QRect = QRect(self.to_qpoint(lu), self.to_qpoint(rd)) 
        painter.drawEllipse(rect)

    @log_method
    def drawGrid(self, painter: QPainter):
        """
        @breif Метод для рисования сетки
        @param painter: объект QPainter для рисования
        """
        for dx in range(0, self.width, DrawConst.scaleX):
            painter.drawLine(dx, 0, dx, self.height)

        for dy in range(0, self.height, DrawConst.scaleY):
            painter.drawLine(0, dy, self.width, dy)

        painter.setPen(Qt.red)
        painter.drawLine(0, self.o_y, self.width, self.o_y)
        painter.drawLine(self.o_x, 0, self.o_x, self.height)

    def mousePressEvent(self, e: QMouseEvent):
        """
        @breif Обработка события нажатия кнопки мыши
        @param e: событие
        """
        t = e.pos()
        qp: QPoint = QPoint(t.x()-10, t.y()-10)
        p = self.to_decart(qp)
        print(f'canvas = {qp}\npoint = {p}')
        print(self.to_qpoint(p))

    def on_canvas(self, pos: QPoint):
        """
        @breif Проверяет, лежит ли точка внутри холста
        @param pos: позиция
        """
        rect: QRect = self.ui.canvas.geometry()
        x = pos.x()
        y = pos.y()
        return (x >= rect.x() and x <= rect.x() + rect.width() and
                y >= rect.y() and y <= rect.y() + rect.height())


    def to_decart(self, qpoint: QPointF):
        """
        @breif Преобразования точки в декартовы координаты
        @param qpoint: точка в координатах холста(пиксели)
        """
        x = (qpoint.x() - self.o_x) / DrawConst.scaleX
        y = (-qpoint.y() + self.o_y) / DrawConst.scaleY
        return Point(x, y)

    def to_qpoint(self, point: Point):
        """
        @breif Преобразования точки в в координаты холста(пиксели)
        @param point: точка в декартовых координатах
        """
        x = point.x() * DrawConst.scaleX + self.o_x
        y = -point.y() * DrawConst.scaleY + self.o_y
        return QPoint(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
