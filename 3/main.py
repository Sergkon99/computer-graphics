import sys
from ui.ui import *
from PyQt5.QtCore import Qt, QPointF, QRect, QPoint, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainter, QPixmap, QColor, QMouseEvent, QPolygon
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication

from utils import *
from geometric import Point
from constants import DrawConst


class MyWin(QMainWindow):
    c = pyqtSignal(Point)
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # размеры холста (ширрина и высота) в пикселях
        self.width = self.ui.canvas.width()
        self.height = self.ui.canvas.height()

        self.o_x = int(self.width * DrawConst.centerX)
        self.o_y = int(self.height * DrawConst.centerY)

        self.c.connect(lambda i: print('pyqtSignal', i))

        self.c.emit(Point(0, 0))
        self._init_canvas(self.width, self.height)

        self.points = []

        self.ui.pb_draw_line.clicked.connect(self.drawBresenhamLine)
        self.ui.pb_draw_circle.clicked.connect(self.drawBresenhamCircle)

    def mousePressEvent(self, event: QMouseEvent):
        pos: QPoint = event.pos()
        rect: QRect = self.ui.canvas.geometry()
        if event.button() == Qt.LeftButton:
            if self.on_canvas(event.pos()):
                decart_pos: Point = self.to_decart(QPoint(pos.x() - rect.x(), pos.y() - rect.y())).int_coords()
                if decart_pos not in self.points:
                    self.points.append(decart_pos)
        elif event.button() == Qt.RightButton:
            if self.on_canvas(event.pos()):
                decart_pos: Point = self.to_decart(QPoint(pos.x() - rect.x(), pos.y() - rect.y())).int_coords()
                if decart_pos in self.points:
                    del_idx = self.points.index(decart_pos)
                    del self.points[del_idx]

        self.draw()

    def on_canvas(self, pos: QPoint):
        """
        Проверяет, лежит ли точка внутри холста
        :param: pos позиция
        """
        rect: QRect = self.ui.canvas.geometry()
        x = pos.x()
        y = pos.y()
        return (x >= rect.x() and x <= rect.x() + rect.width() and
                y >= rect.y() and y <= rect.y() + rect.height())

    def _init_canvas(self, w, h):
        """
        Начальная инициализиция холста
        :param: w ширина холста
        :param: h высота холста
        """
        self.pixmap = QPixmap(w, h)
        self.pixmap.fill(Qt.white)
        painter = QPainter()
        painter.begin(self.pixmap)

        self.drawCanvas(painter)

        a: Point = Point(0, 0)
        b: Point = Point(-3, -6)
        # self.drawLine(painter, a, b)
        # self.BresenhamLine(painter, a, b)
        # self.drawEllipse(painter, a, 4)
        # self.BresenhamCircle(painter, a, 4)

        painter.end()

        self.setPixmap()

    def draw(self):
        self.clearCanvas()

        painter = QPainter()
        painter.begin(self.pixmap)

        self.drawCanvas(painter)

        if len(self.points) > 1:
            for p1, p2 in zip(self.points[1:], self.points[:-1]):
                self.drawLine(painter, p1, p2)
                self.BresenhamLine(painter, p1, p2)

        for point in self.points:
            self.drawPoint(painter, point)

        painter.end()

        self.setPixmap()

    def drawBresenhamLine(self):
        self.clearCanvas()

        x1 = int(self.ui.le_line_x1.text())
        y1 = int(self.ui.le_line_y1.text())
        x2 = int(self.ui.le_line_x2.text())
        y2 = int(self.ui.le_line_y2.text())

        painter = QPainter()
        painter.begin(self.pixmap)

        self.drawCanvas(painter)

        self.drawLine(painter, Point(x1, y1), Point(x2, y2))
        self.BresenhamLine(painter, Point(x1, y1), Point(x2, y2))

        painter.end()

        self.setPixmap()

    def drawBresenhamCircle(self):
        self.clearCanvas()

        x = int(self.ui.le_circle_x.text())
        y = int(self.ui.le_circle_y.text())
        r = int(self.ui.le_circle_r.text())

        painter = QPainter()
        painter.begin(self.pixmap)

        self.drawCanvas(painter)

        self.drawEllipse(painter, Point(x, y), r)
        self.BresenhamCircle(painter, Point(x, y), r)

        painter.end()

        self.setPixmap()

    def BresenhamLine(self, painter, a: Point, b: Point):
        x1, y1 = a.x(), a.y()
        x2, y2 = b.x(), b.y()
        dx = x2 - x1
        dy = y2 - y1

        sign_x = 1 if dx>0 else -1 if dx<0 else 0
        sign_y = 1 if dy>0 else -1 if dy<0 else 0

        if dx < 0: dx = -dx
        if dy < 0: dy = -dy

        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy
        
        x, y = x1, y1
        
        error, t = el, 0
        
        self.drawPoint(painter, Point(x, y), Qt.red)
        
        while t < el:
            error -= 2*es
            if error < 0:
                error += 2*el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            self.drawPoint(painter, Point(x, y), Qt.red)

    def BresenhamCircle(self, painter, a: Point, r: int):
        x, y = r, 0
        error = 1 - x
        while x >= y:
            self.drawPoint(painter, Point(x + a.x(), y + a.y()))
            self.drawPoint(painter, Point(y + a.x(), x + a.y()))
            self.drawPoint(painter, Point(-x + a.x(), y + a.y()))
            self.drawPoint(painter, Point(-y + a.x(), x + a.y()))
            self.drawPoint(painter, Point(-x + a.x(), -y + a.y()))
            self.drawPoint(painter, Point(-y + a.x(), -x + a.y()))
            self.drawPoint(painter, Point(x + a.x(), -y + a.y()))
            self.drawPoint(painter, Point(y + a.x(), -x + a.y()))
            
            y += 1
            if error < 0:
                error += 2*y + 1
            else:
                x -= 1
                error += 2*(y - x + 1)

    def drawCanvas(self, painter: QPainter):
        pen = painter.pen()
        painter.setPen(Qt.gray)
        if DrawConst.grid:
            self.drawGrid(painter)
        if DrawConst.axes:
            self.drawAxes(painter)
        painter.setPen(pen)

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
        pen = painter.pen()
        # print(dir(pen))
        painter.setPen(Qt.black)
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

        painter.setPen(pen)

    def drawLine(self, painter: QPainter, a: Point, b: Point):
        painter.drawLine(self.to_qpoint(a), self.to_qpoint(b))

    def drawPoint(self, painter: QPainter, a: Point, color: QColor=Qt.black):
        painter.setPen(color)
        painter.setBrush(color)
        painter.drawEllipse(self.to_qpoint(a), 2, 2)
        # painter.drawPoint(self.to_qpoint(a))
        painter.setBrush(Qt.NoBrush)
        painter.setPen(Qt.black)

    def drawEllipse(self, painter: QPainter, a: Point, r: int):
        painter.drawEllipse(self.to_qpoint(a), r*DrawConst.scaleX, r*DrawConst.scaleY)

    def setPixmap(self):
        """
        Установить pixmap на lable(холст)
        """
        self.ui.canvas.setPixmap(self.pixmap)

    def clearCanvas(self):
        """
        Очистить холст глобально
        """
        self.pixmap.fill(Qt.white)
        self.setPixmap()

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