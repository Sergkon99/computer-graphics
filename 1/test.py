import unittest
# import src.on2d as on2d, src.on3d as on3d
from src.utils import intersects, on_once_line
from src.on2d import Point as Point2D, Line as Line2D, Position, Segment as Segment2D, Ray as Ray2D
from src.on3d import Point as Point3D, Line as Line3D, Vector as Vector3D, Angle as Angle3D, AngleType
from src.exceptions import *

class TestGeom(unittest.TestCase):

    def test_line(self):
        l1 = Line2D(a=-1, b=2, c=-3)
        l2 = Line2D(a=2, b=-4, c=6)
        rp = l1.position(l2)
        self.assertEqual(rp, Position.match)

        l1 = Line2D(a=2, b=-1, c=5)
        l2 = Line2D(a=2, b=-1, c=-11)
        rp = l1.position(l2)
        self.assertEqual(rp, Position.parallel)

        l1 = Line2D(a=4, b=3, c=-1)
        l2 = Line2D(a=5, b=-2, c=3)
        rp = l1.position(l2)
        self.assertEqual(rp, Position.intersect)

        l1 = Line2D(a=0, b=1, c=-1)
        l2 = Line2D(a=5, b=-2, c=3)
        rp = l1.position(l2)
        self.assertEqual(rp, Position.intersect)

        l1 = Line2D(a=0, b=1, c=-1)
        l2 = Line2D(a=0, b=-2, c=2)
        rp = l1.position(l2)
        self.assertEqual(rp, Position.match)

        l1 = Line2D(a=3, b=0, c=-1)
        l2 = Line2D(a=1, b=0, c=2)
        rp = l1.position(l2)
        self.assertEqual(rp, Position.parallel)

        with self.assertRaises(LineNotExists):
            Line2D(a=0, b=0, c=1)

    def test_intersect(self):
        a = Point2D()
        b = Point2D(x=3)
        c = Point2D(x=2)
        d = Point2D(x=4)
        s = Segment2D(c, d)
        r = Ray2D(a, b)
        res = intersects(s=s, r=r)
        self.assertTrue(res)

        r = Ray2D(b, a)
        res = intersects(s=s, r=r)
        self.assertTrue(res)

        c = Point2D(x=5)
        d = Point2D(x=7)
        s = Segment2D(a, b)
        res = intersects(s=s, r=r)
        self.assertTrue(res)

        a = Point2D(x=5)
        b = Point2D(x=8)
        c = Point2D()
        d = Point2D(x=1)
        s = Segment2D(c, d)
        r = Ray2D(a, b)
        res = intersects(s=s, r=r)
        self.assertFalse(res)

        a = Point2D()
        b = Point2D(x=3, y=3)
        c = Point2D(x=5, y=5)
        d = Point2D(x=7, y=7)
        s = Segment2D(c, d)
        r = Ray2D(a, b)
        res = intersects(s=s, r=r)
        self.assertTrue(res)

        c = Point2D(x=-3, y=-3)
        d = Point2D(x=-5, y=-5)
        s = Segment2D(c, d)
        res = intersects(s=s, r=r)
        self.assertFalse(res)

        a = Point2D(x=0, y=1)
        b = Point2D(x=0, y=3)
        c = Point2D(x=0, y=5)
        d = Point2D(x=0, y=7)
        r = Ray2D(a, b)
        s = Segment2D(c, d)
        res = intersects(s=s, r=r)
        self.assertTrue(res)

        r = Ray2D(c, d)
        s = Segment2D(a, b)
        res = intersects(s=s, r=r)
        self.assertFalse(res)

        b = Point2D(x=0, y=5)
        r = Ray2D(c, d)
        s = Segment2D(a, b)
        res = intersects(s=s, r=r)
        self.assertTrue(res)

        b = Point2D(x=1, y=4)
        r = Ray2D(c, d)
        s = Segment2D(a, b)
        with self.assertRaises(InputError):
            res = intersects(s=s, r=r)

    def test_angle(self):
        a = Point3D(x=2, y=0, z=-1)
        b = Point3D(x=0, y=0, z=0)
        c = Point3D(x=1, y=2, z=3)
        t_angle = Angle3D(a, b, c).type()
        self.assertEqual(t_angle, AngleType.Obtuse)

        a = Point3D(x=5, y=0, z=0)
        b = Point3D(x=0, y=0, z=0)
        c = Point3D(x=1, y=5, z=0)
        t_angle = Angle3D(a, b, c).type()
        self.assertEqual(t_angle, AngleType.Acute)

        a = Point3D(x=5, y=0, z=0)
        b = Point3D(x=0, y=0, z=0)
        c = Point3D(x=0, y=5, z=0)
        t_angle = Angle3D(a, b, c).type()
        self.assertEqual(t_angle, AngleType.Right)

        a = Point3D(x=5, y=0, z=0)
        b = Point3D(x=0, y=0, z=0)
        c = Point3D(x=-1, y=5, z=0)
        t_angle = Angle3D(a, b, c).type()
        self.assertEqual(t_angle, AngleType.Obtuse)

    def test_cross_product3d(self):
        a = Vector3D().from_coords(x=-1, y=2, z=-3)
        b = Vector3D().from_coords(x=0, y=-4, z=1)
        c = a.cross(b)
        # print(a, b, c, sep='\n')
        t1 = a.dot(c)
        t2 = b.dot(c)
        # print(t1, t2)

    def test_1(self):
        a = Point3D()
        b = Point3D(x=10)
        c = Point3D(x=4)
        d = Point3D(x=4, y=1)
        ab = Vector3D(a, b)
        ac = Vector3D(a, c)
        ad = Vector3D(a, d)
        # print(ab.len())
        # print(ab.cross(ac).len())
        # print(ab.cross(ad).len())

    def test_2(self):
        a = Point2D(x=0, y=1)
        b = Point2D(x=2, y=2)
        l = Line2D().from_points(a, b)
        print(l)

    def test_once_line(self):
        a = Point3D()
        b = Point3D(x=0, y=1)
        c = Point3D(x=0, y=4)
        res = on_once_line(a, b, c)
        self.assertTrue(res)

        c = Point3D(x=3, y=4)
        res = on_once_line(a, b, c)
        self.assertFalse(res)

        a = Point3D(x=1, y=1, z=1)
        b = Point3D(x=2, y=2, z=2)
        c = Point3D(x=3, y=3, z=3)
        res = on_once_line(a, b, c)
        self.assertTrue(res)

        c= Point3D(x=3, y=3, z=4)
        res = on_once_line(a, b, c)
        self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()
