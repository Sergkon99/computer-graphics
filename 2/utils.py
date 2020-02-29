import time
from functools import wraps

def log_method(func):
    # Декоратор логгирования
    @wraps(func)
    def wrap(self, *args, **kwargs):
        start = time.time()
        print(f'[Start] "{func.__name__}"')
        res = func(self, *args, **kwargs)
        print(f'[Working] "{func.__name__}" {round((time.time() - start)*1000, 2)} ms')
        print(f'[End] "{func.__name__}"')
        return res
    return wrap


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

    def __str__(self):
        return f'({self._x} {self._y})'
