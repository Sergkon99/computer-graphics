from math import sin, cos, pi

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
    grid = 1
    axes = 1
    # отступ для фигуры
    r = 3
    # смещение фигуры относитльно (0, 0)
    dx = 0
    dy = 0
