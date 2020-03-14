import time
from functools import wraps
from algebraic import *
from geometric import *
from math import sin, cos, pi
from constants import DrawConst

def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step

def generate_rhomb():
    r, dx, dy = DrawConst.r, DrawConst.dx, DrawConst.dy
    return [(-r+dx, 0+dy), (0+dx, r+dy),(r+dx, 0+dy), (0+dx, -r+dy)]

def generate_rect():
    r, dx, dy = DrawConst.r, DrawConst.dx, DrawConst.dy
    return [(-r+dx, r+dy), (r+dx, r+dy), (r+dx, -r+dy), (-r+dx, -r+dy)]

def generate_circle():
    r, dx, dy = DrawConst.r, DrawConst.dx, DrawConst.dy
    return [(r*cos(t) + dx, r*sin(t) + dy) for t in frange(0, 2*pi, 0.01)]

def generate_star():
    r, dx, dy = DrawConst.r, DrawConst.dx, DrawConst.dy
    n, a = 5, pi/2
    return [(r*cos(a+2*k*pi/n) + dx, r*sin(a+2*k*pi/n) + dy) for k in range(n)]

def generate_figure():
    r, dx, dy = DrawConst.r, DrawConst.dx, DrawConst.dy
    # генерируем точки на окружности
    figure = [(r*cos(t)+dx, r*sin(t)+dy) for t in frange(0, 2*pi, 0.01)]
    # задем прямые
    figure.extend([(-r+dx, dy) ,(r+dx, dy)])
    figure.extend([(dx, -r+dy) ,(dx, r+dy)])

    return figure

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

def rotate(p: Point, angle: float):
    """
    @breif Метод для поворота точки на угол
    @param p: точка
    @param angle: угол
    @return Точка-результат
    """
    angle = angle*pi/180
    rotate = Matrix([
        [cos(angle), sin(angle), 0],
        [-sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])
    vector = to_vector(p)
    return to_point(rotate*vector)

def rotate_from(p: Point, angle: float, x: Point):
    """
    @breif Метод для поворота точки на угол относитьльно другой точки
    @param p: точка
    @param angle: угол
    @param x: точка отсчета
    @return Точка-результат
    """
    angle = angle*pi/180
    move_to = Matrix([
        [1, 0, x.x()],
        [0, 1, x.y()],
        [0, 0, 1]
    ])
    move_from = Matrix([
        [1, 0, -x.x()],
        [0, 1, -x.y()],
        [0, 0, 1]
    ])
    rotate = Matrix([
        [cos(angle), sin(angle), 0],
        [-sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])
    vector = to_vector(p)
    return to_point(move_to*rotate*move_from*vector)


