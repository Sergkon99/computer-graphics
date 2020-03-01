from typing import List

class Matrix:
    """
    Алгебраическая матрица
    """
    def __init__(self, rows: List[List]=None, n: int=None, m: int=None):
        if rows:
            # Матрица на основе переднанного двумерного списка
            self._rows = rows
            if len(rows) == 0:
                raise Exception('Empty list')
            cnt_rows = len(self._rows[0])
            for row in self._rows:
                if len(row) != cnt_rows:
                    raise Exception('lenghts in rows not equal')
        elif n and m:
            # Нулевая матрица по переданным размерам
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

    def __repr__(self):
        return str(self._rows)

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