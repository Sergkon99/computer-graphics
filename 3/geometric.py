from __future__ import annotations
from math import floor, ceil

class Point:
    """
    Вспомогательный класс точки в декартовых коордмнатах
    """
    def __init__(self, x: float=0, y: float=0):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.__from_coord(x, y)
        elif isinstance(x, tuple):
            self.__from_pair(x)
        else:
            raise ValueError('Overload not exsists')

    def __from_coord(self, x, y):
        """
        @breif "Конструктор" из координат
        @return Point
        """
        self._x: float = x
        self._y: float = y

    def __from_pair(self, pair):
        """
        @breif "Конструктор" из пары(кортеж), задающей координаты
        @return Point
        """
        self._x: float = pair[0]
        self._y: float = pair[1]

    def x(self):
        return self._x

    def y(self):
        return self._y

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def int_coords(self):
        return Point(int(round(self._x, 0)), int(round(self._y, 0)))

    def __eq__(self: Point, other: Point):
        return self._x == other._x and self._y == other._y

    def __str__(self):
        return f'({self._x} {self._y})'


class GeometricVector:
    """
    Класс вектора
    P.S. похоже не нужен
    """
    def __init__(self, x, y, z=1):
        self._x = x
        self._y = y
        self._z = z

    def x(self):
        return self._x

    def y(self):
        return self._y

    def z(self):
        return self._z

    def __add__(self, v):
        return GeometricVector(self._x + v.x(),
                      self._y + v.y(),
                      self._z + v.z())

    def __str__(self):
        return f'({self.x()},{self.y()},{self.z()})'

    def __mul__(self, n):
        if isinstance(n, (float, int)):
            return GeometricVector(n*self.x(), n*self.y())
        raise ValueError('')
    
    def __rmul__(self, n):
        if isinstance(n, (float, int)):
            return self.__mul__(n)
        raise ValueError('')