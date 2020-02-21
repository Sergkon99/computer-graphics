from enum import Enum


class LineNotExists(Exception):
    pass


class Point():
    # точка с координатами (x, y)
    def __init__(self, *, x, y):
        self.x: float = x
        self.y: float = y

    def __str__(self) -> str:
        return f'({self.x},{self.y})'


class Position(Enum):
    parallel = 1   # параллельны
    intersect = 2  # пересекаются
    match = 3      # совпадают


class Line():
    # прямая вида ax + by + c = 0
    def __init__(self, *, a, b, c):
        if a == 0 and b == 0:
            raise LineNotExists('a and b equal zero')
        self.a = a
        self.b = b
        self.c = c
        # вектор нормали
        # self.n = Vector(a, b)

    def __str__(self) -> str:
        return f'{self.a}x + {self.b}y + {self.c} = 0'

    def position(self, line: 'Line') -> Position:
        eps = 10**-3
        if abs(self.a*line.b - self.b*line.a) > eps:
            return Position.intersect
        if (abs(self.a*line.b - self.b*line.a) < eps and
            abs(self.b*line.c - self.c*line.b) < eps and
            abs(self.a*line.c - self.c*line.a) < eps):
            return Position.match
        return Position.parallel


class Vector():
    # вектор из точки a в точку b
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b
        # координаты вектора
        self.x = b.x - a.x
        self.y = b.y - a.y

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