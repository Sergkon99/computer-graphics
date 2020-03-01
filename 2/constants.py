from math import sin, cos, pi
from enum import Enum

def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step

class DrawConst:
    # кол-во пикселей на клетку
    scaleX = 20
    scaleY = 20
    # координаты центра в %
    centerX = 0.5
    centerY = 0.5
    # координатный осей
    xmin = -3
    xmax = 3
    ymin = -3
    ymax = 3
    # для холста
    grid = False
    axes = True
    # отступ для фигуры
    r = 3
    # смещение фигуры относитльно (0, 0)
    dx = 0
    dy = 0
    rect = [(-r, r), (r, r), (r, -r), (-r, -r)]
    circle = [(3*cos(t), 3*sin(t)) for t in frange(0, 2*pi, 0.01)]
    rhomb = [(-r, 0), (0, r),(r, 0), (0, -r)]

class FigureType(Enum):
    none = 0
    my = 1
    rect = 2
    rhomb = 3
    circle = 4
    star = 5