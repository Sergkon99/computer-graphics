import time
from functools import wraps
from typing import List

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


class GeometricVector:
    """
    Класс вектора
    P.S. похоже не нужен
    """
    def __init__(self, x, y, z=0):
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


class Matrix:
    """
    Алгебраическая матрица
    """
    def __init__(self, rows: List[List]=None, n: int=None, m: int=None):
        if rows:
            self._rows = rows
            if len(rows) == 0:
                raise Exception('Empty list')
            cnt_rows = len(self._rows[0])
            for row in self._rows:
                if len(row) != cnt_rows:
                    raise Exception('lenghts in rows not equal')
        elif n and m:
            self._rows = [[0 for _ in range(m)] for _ in range(n)]
        else:
            ValueError('Overload not exists')

    def size(self):
        """
        @breif Вернент пару - размеры матрицы
        @return число строк и число столбцов
        """
        return (len(self._rows), len(self._rows[0]))

    def __mul__(self, other):
        """
        @breif Оператор умножения для матрицы
        @info Выполнится, если число столбцов в первой матрице равно числу строк во второй
        @return матрица-результат
        """
        if self.size()[1] != other.size()[0]:
            raise Exception('Count rows and clomns not equal')
        n = self.size()[0]   # число строк в первой
        q = self.size()[1]   # число столбцов в первой
        m = other.size()[1]  # число столбцов во второй
        res = Matrix(n=n, m=m)
        for i in range(n):
            for j in range(m):
                for k in range(q):
                    res[i][j] += self[i][k] * other[k][j]
        return res

    def __add__(self, other):
        """
        @breif Оператор сложения для матрицы
        @info Выполнится, если матрицы имеют одинаковые размеры
        @return матрица-результат 
        """
        if self.size() != other.size():
            raise ValueError('Different matrxis')
        res = Matrix(n=self.size()[0], m=self.size()[1])
        for i in range(res.size()[0]):
            for j in range(res.size()[1]):
                res[i][j] = self[i][j] + other[i][j]
        return res

    def __getitem__(self, key):
        return self._rows[key]

    def __eq__(self, other):
        if self.size() != other.size():
            return False
        for i in range(self.size()[0]):
            if self[i] != other[i]:
                return False
        return True

    def __str__(self):
        s = ''
        for row in self._rows:
            s += ' '.join(map(str, row)) + '\n'
        return s


class Vector(Matrix):
    """
    Вектор-столбец
    """
    def __init__(self, col: List):
        matrix = [[x] for x in col]
        super().__init__(matrix)
