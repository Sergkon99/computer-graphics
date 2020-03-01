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
    dx = -1
    dy = 1
    figure = [(-r+dx, 0+dy), (0+dx, r+dy), (r+dx, 0+dy), (0+dx, -r+dy), (dx, dy)]