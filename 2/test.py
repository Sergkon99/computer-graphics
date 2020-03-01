import unittest

from algebraic import Matrix, Vector
from utils import *

class TestGeom(unittest.TestCase):
    def test_mul_matrix(self):
        a = Matrix([
            [1, 2, 2],
            [3, 4, 4]
            ])
        b = Matrix([
            [1, 2],
            [3, 4],
            [1, 1]
        ])
        c = Matrix([
            [9, 12],
            [19, 26]
        ])
        self.assertEqual(a*b, c)

        a = Matrix([
            [4, 2],
            [9, 0]
        ])
        b = Matrix([
            [3, 1],
            [-3, 4]
        ])
        c= Matrix([
            [6, 12],
            [27, 9]
        ])
        self.assertEqual(a*b, c)

    def test_sum_matrix(self):
        a = Matrix([
            [4, 2],
            [9, 0]
        ])
        b = Matrix([
            [3, 1],
            [-3, 4]
        ])
        c= Matrix([
            [7, 3],
            [6, 4]
        ])
        self.assertEqual(a+b, c)

    def test_mul_vector_matrix(self):
        a = Matrix([
            [2, 4, 0],
            [-2, 1, 3],
            [-1, 0, 1]
        ])
        b = Vector([1, 2, -1])
        c = Vector([10, -3, -2])
        self.assertEqual(a*b, c)

        a = Vector([3, 2, 0, 1])
        b = Matrix([
            [-1, 1, 0, 2]
        ])
        c = Matrix([
            [-3, 3,0, 6],
            [-2, 2, 0, 4],
            [0, 0, 0, 0],
            [-1, 1, 0, 2]
        ])
        self.assertEqual(a*b, c)

    def test_1(self):
        a = Matrix([
            [2, 4, 0],
            [-2, 1, 3],
            [-1, 0, 1]
        ])
        # print(repr(a))
        p = Point(2, 3)
        v = to_vector(p)
        print(v)
        g = GeometricVector(3, 4)
        # v = move_to(p, g)
        print(v[0], v[1])
        print(repr(v))
        p = to_point(v)
        print(p)


if __name__ == "__main__":
    unittest.main()