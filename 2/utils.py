import time
from functools import wraps
from algebraic import *
from geometric import *

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

def to_vector(p: Point):
    """Преобразование точки в вектор"""
    return Vector([p.x(), p.y(), 1])

def to_point(v: Vector):
    """Преобразование вектора в точку"""
    return Point(v[0][0], v[1][0])

def move_on(p: Point, x: float, y: float):
    """
    @breif Смещение на (x, y) в декартовых координатах
    @param x, y смещение
    @return точка в декартовых координатах
    """
    move = Matrix([
        [1, 0, x],
        [0, 1, y],
        [0, 0, 1]
    ])
    vector = to_vector(p)
    return to_point(move*vector)