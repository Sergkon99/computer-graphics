import sys
from ui.ui import *
from PyQt5.QtCore import Qt, QPointF, QRect, QPoint
from PyQt5.QtGui import QPainter, QPixmap, QColor, QMouseEvent, QPolygon
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
# from PyQt5.QtCore.QEvent import QMouseEvent
import random
from utils import *
from geometric import Point
from constants import DrawConst
from typing import List
from functools import partial


class MyWin(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.figure = list(map(Point, DrawConst.figure))
        self.figure = generate_figure()
        self.global_state = self.figure.copy()
        # print(self.figure)

        # размеры холста (ширрина и высота) в пикселях
        self.width = self.ui.canvas.width()
        self.height = self.ui.canvas.height()
        # print(f'width={self.width}\nheight={self.height}')

        # координаты центра(0, 0) в координатах холста(в пикселях)
        self.o_x = int(self.width * DrawConst.centerX)
        self.o_y = int(self.height * DrawConst.centerY)
        # нужно ли запоминать промежуточные состояния
        self.state: bool = self.ui.cb_global_figure.isChecked()

        # инициализируем холст
        self.__init_canvas(self.width, self.height)
        self.defaultPos()

        # связываем клик с вызовом функции
        self.ui.pb_default.clicked.connect(self.defaultPos)
        self.ui.pb_move_x.clicked.connect(self.moveFigureX)
        self.ui.pb_move_y.clicked.connect(self.moveFigureY)
        self.ui.pb_reflection_x.clicked.connect(self.reflectionX)
        self.ui.pb_reflection_y.clicked.connect(self.reflectionY)
        self.ui.pb_reflection_xy.clicked.connect(self.reflectionXY)
        self.ui.pb_scale.clicked.connect(self.scale)
        self.ui.pb_rotate.clicked.connect(self.rotate)
        # события ui элементов
        self.ui.le_move.inputRejected.connect(lambda : print('line edit event'))
        self.ui.cb_global_figure.stateChanged.connect(self.changeGlobal)

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

        if DrawConst.axes:
            self.drawAxes(painter)
        if DrawConst.grid:
            self.drawGrid(painter)

        painter.end()

        self.setPixmap()

    def changeGlobal(self):
        """
        Изменить флаг о сохранении промежуточных состояниях при смене состояния chex box-a (по событию)
        """
        self.state: bool = self.ui.cb_global_figure.isChecked()
        # print(self.state)

    def clearCanvas(self):
        """
        Очистить холст глобально
        """
        self.pixmap.fill(Qt.white)
        self.setPixmap()

    def setPixmap(self):
        """
        Установить pixmap на lable(холст)
        """
        self.ui.canvas.setPixmap(self.pixmap)

    def _get_figure(self):
        return self.global_state if self.state else self.figure

    def defaultPos(self):
        """
        Нарисовать фигуру на дефолтной позиции
        """
        if self.state:
            self.global_state = self.figure.copy()
        self.drawFigure(self.figure)

    def drawMovedFigure(self, x, y):
        """
        @breif Нарисовать смещенную фигуру
        @param x, y на сколько сместить по каждой из осей в декартовых координатах
        """
        p_move_on = partial(move_on, x=x, y=y)
        figure = list(map(p_move_on, self._get_figure()))
        self.drawFigure(figure)

    def moveFigureX(self):
        """
        Сместить фигуру по оси x
        """
        try:
            dx = int(self.ui.le_move.text())
            self.drawMovedFigure(int(dx), 0)
        except ValueError as ex:
            self.ui.le_move.setText('')
            print(ex)
        except Exception as ex:
            print('Unknown error: ' + str(ex))

    def moveFigureY(self):
        """
        Сместить фигуру по оси y
        """
        try:
            dy = int(self.ui.le_move.text())
            self.drawMovedFigure(0, int(dy))
        except ValueError as ex:
            self.ui.le_move.setText('')
            print(ex)
        except Exception as ex:
            print('Unknown error: ' + str(ex))

    def reflectionX(self):
        """
        Отразит фигуру относительно оси х
        """
        reflection_x = partial(reflection, x=True, y=False)
        figure = list(map(reflection_x, self._get_figure()))
        self.drawFigure(figure)

    def reflectionY(self):
        """
        Отразит фигуру относительно оси y
        """
        reflection_y = partial(reflection, x=False, y=True)
        figure = list(map(reflection_y, self._get_figure()))
        self.drawFigure(figure)

    def reflectionXY(self):
        """
        Отразит фигуру относительно прямой X=Y
        """
        reflection_xy = partial(reflection, x=True, y=True)
        figure = list(map(reflection_xy, self._get_figure()))
        self.drawFigure(figure)

    def scale(self):
        """
        Метод для отрисовки масштабирования
        """
        try:
            scale_x = float(self.ui.le_scale_x.text() or 1)
            scale_y = float(self.ui.le_scale_y.text() or 1)
            scale_xy = partial(scale, x=scale_x, y=scale_y)
            figure = list(map(scale_xy, self._get_figure()))
            self.drawFigure(figure)
        except ValueError as ex:
            self.ui.le_scale_x.setText('')
            self.ui.le_scale_y.setText('')
            print(str(ex))
        except Exception as ex:
            print('Unknown error: ' + str(ex))

    def rotate(self):
        """
        Метод для поворота фигуры относительно (0, 0)
        """
        try:
            angle = float(self.ui.le_rotate_angle.text())
            p_rotate = partial(rotate, angle=angle)
            figure = list(map(p_rotate, self._get_figure()))
            self.drawFigure(figure)
        except ValueError as ex:
            self.ui.le_rotate_angle.setText('')
            print(str(ex))
        except Exception as ex:
            print('Unknown error: ' + str(ex))

    @log_method
    def drawFigure(self, figure: List[Point], event=None):
        """
        @breif Основной метод для рисования фигуры
        @param event: без него не работает декоратор, возможно про срабатывании события что-то передаются
        """
        # Сохраним глобальное состояние фигуры, если нужно
        if self.state:
            self.global_state = figure.copy()
        # Очистим холст перед рисованием
        self.clearCanvas()
        painter = QPainter()
        painter.begin(self.pixmap)

        if DrawConst.axes:
            self.drawAxes(painter)
        if DrawConst.grid:
            self.drawGrid(painter)

        painter.setPen(Qt.red)

        # Посление 4 точки задают прямые(так сгенерировано)
        self.drawEllipse(painter, figure[:-4])
        self.drawLine(painter, figure[-2], figure[-1])
        self.drawLine(painter, figure[-4], figure[-3])

        painter.end()
        self.setPixmap()

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
    def drawEllipse(self, painter: QPainter, figure: List[Point]):
        """
        @breif Метод для рисования эллипса
        @param painter: объект QPainter для рисования
        @param figure: точки, задающие зллипс
        @info При поворте эллипса упираемся в то, что нельзя задать наклонный прямоугольник
              !Все методы рисуют эллипс с осями, паралельными координатным осям
              Повернуть его без использования встроенных функций невозможно
        """
        polygon: QPolygon = QPolygon(list(map(self.to_qpoint, figure[:-4])))
        painter.drawPolygon(polygon)

    def drawGrid(self, painter: QPainter):
        """
        @breif Метод для рисования сетки
        @param painter: объект QPainter для рисования
        """
        for dx in range(0, self.width, DrawConst.scaleX):
            painter.drawLine(dx, 0, dx, self.height)

        for dy in range(0, self.height, DrawConst.scaleY):
            painter.drawLine(0, dy, self.width, dy)

    def drawAxes(self, painter: QPainter):
        """
        @breif Метод для рисования осей с подписями
        @param painter: объект QPainter для рисования
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


    def to_decart(self, qpoint: QPoint):
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
