import math
from enum import Enum


class Point():
    # точка с координатами (x, y, z)
    def __init__(self, *, x=0, y=0, z=0):
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def __str__(self) -> str:
        return f'({self.x},{self.y},{self.z})'


class Vector():
    # вектор из точки a в точку b
    def __init__(self, a: Point=Point(), b: Point=Point()):
        # координаты вектора
        self.x = b.x - a.x
        self.y = b.y - a.y
        self.z = b.z - a.z

    def from_coords(self, *, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return self

    def __str__(self):
        return f'({self.x};{self.y};{self.z})'

    def len(self):
        return self.dot(self)**(1/2)

    def dot(self, v: 'Vector'):
        # скалярное произведение
        return self.x * v.x + self.y * v.y + self.z * v.z

    def cross(self, v: 'Vector'):
        # [self x v]
        # векторное произведение
        return Vector().from_coords(
            x=self.y * v.z - self.z * v.y,
            y=self.z * v.x - self.x * v.z,
            z=self.x * v.y - self.y * v.x
        )
        # self.x * v.y - self.y * v.x


class AngleType(Enum):
    Acute = 1  # острый
    Right = 2  # прямой
    Obtuse = 3 # тупой


class Angle():
    # угол построенный на 3-ч точках, b - вершина
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def angle(self):
        ba = Vector(self.b, self.a)
        bc = Vector(self.b, self.c)
        cosa = ba.dot(bc)/ba.len()/bc.len()
        return round(math.acos(cosa)*180/math.pi)

    def type(self):
        angle = self.angle()
        if angle < 90:
            return AngleType.Acute
        elif angle > 90:
            return AngleType.Obtuse
        else:
            return AngleType.Right


class Line():
    def __init__(self, *, a: Point, b: Point):
        self.a = a
        self.b = b
        # направляющий вектор
        self.v = Vector(a, b)
