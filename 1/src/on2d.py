from enum import Enum
from .exceptions import LineNotExists


class Point():
    # точка с координатами (x, y)
    def __init__(self, *, x=0, y=0):
        self.x: float = x
        self.y: float = y

    def __str__(self) -> str:
        return f'({self.x},{self.y})'



class Vector():
    # вектор из точки a в точку b
    def __init__(self, a: Point=Point(), b: Point=Point()):
        self.a = a
        self.b = b
        # координаты вектора
        self.x = b.x - a.x
        self.y = b.y - a.y

    def from_coords(self, *, x, y):
        self.x = x
        self.y = y
        return self

    def __str__(self):
        return f'({self.x};{self.y})'

    def len(self):
        return self.dot(self)**(1/2)

    def dot(self, v: 'Vector'):
        # скалярное произведение
        return self.x * v.x + self.y * v.y

    def cross(self, v: 'Vector'):
        # векторное произведение
        return self.x * v.y - self.y * v.x


class Position(Enum):
    parallel = 1   # параллельны
    intersect = 2  # пересекаются
    match = 3      # совпадают


class Line():
    # прямая вида ax + by + c = 0
    def __init__(self, *, a: float=None, b: float=None, c: float=None):
        if a == 0 and b == 0:
            raise LineNotExists('a and b equal zero')
        self.a = a or 0
        self.b = b or 0
        self.c = c or 0
        # вектор нормали
        self.n = Vector().from_coords(x=a, y=b)

    def from_points(self, a: Point, b: Point):
        self.n = Vector(a, b)
        self.a = -self.n.y
        self.b = self.n.x
        self.c = -(self.a*a.x + self.b*a.y)
        return self

    def __str__(self) -> str:
        return f'{self.a}x + {self.b}y + {self.c} = 0'

    def position(self, line: 'Line') -> Position:
        # вернет взамиорасполежение текущей прямой с переданной
        eps = 10**-3
        if abs(self.a*line.b - self.b*line.a) > eps:
            return Position.intersect
        if (abs(self.a*line.b - self.b*line.a) < eps and
            abs(self.b*line.c - self.c*line.b) < eps and
            abs(self.a*line.c - self.c*line.a) < eps):
            return Position.match
        return Position.parallel

    def belongs(self, p: Point):
        # проверит, принадлежит ли точка прямой
        return self.a*p.x + self.b*p.y + self.c == 0


class Segment():
    # отрезок [a, b]
    def __init__(self, a: Point=Point(), b: Point=Point()):
        self.a = a
        self.b = b


class Ray():
    # луч вида [a, b)
    def __init__(self, a: Point=Point(), b: Point=Point()):
        self.a = a
        self.b = b

