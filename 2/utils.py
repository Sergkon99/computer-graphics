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

def reflection(p: Point, x: bool=False, y:bool=False):
    """
    @breif Выполнит отражение точки относитьльно осей Ox, Oy или прямой X=Y
    @param p: Точка
    @param x, y: Показывает как производит отображение: 
            x==True and x==False - относительно Ox
            x==False and x==True - относительно Oy
            x==True and x==True - относительно X=Y
    @return Точка-результат
    """
    ref_x = Matrix([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ])
    ref_y = Matrix([
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    ref_xy = Matrix([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 1]
    ])
    vector = to_vector(p)
    if x and y:
        return to_point(ref_xy*vector)
    elif x:
        return to_point(ref_x*vector)
    elif y:
        return to_point(ref_y*vector)
    raise RuntimeError('Unknown reflection')

def scale(p: Point, x: float=1, y: float=1):
    """
    @breif Мастабирование по осям
    @param x, y: Коэффиценты масшиабирования по осям соответсвенно
    @return тока-результат
    """
    scale = Matrix([
        [x, 0, 0],
        [0, y, 0],
        [0, 0, 1]
    ])
    vector = to_vector(p)
    return to_point(scale*vector)

