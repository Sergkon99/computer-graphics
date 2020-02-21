import unittest
import on2d, on3d

class TestGeom(unittest.TestCase):

    def test_line(self):
        l1 = on2d.Line(a=-1, b=2, c=-3)
        l2 = on2d.Line(a=2, b=-4, c=6)
        rp = l1.position(l2)
        self.assertEqual(rp, on2d.Position.match)

        l1 = on2d.Line(a=2, b=-1, c=5)
        l2 = on2d.Line(a=2, b=-1, c=-11)
        rp = l1.position(l2)
        self.assertEqual(rp, on2d.Position.parallel)

        l1 = on2d.Line(a=4, b=3, c=-1)
        l2 = on2d.Line(a=5, b=-2, c=3)
        rp = l1.position(l2)
        self.assertEqual(rp, on2d.Position.intersect)

        l1 = on2d.Line(a=0, b=1, c=-1)
        l2 = on2d.Line(a=5, b=-2, c=3)
        rp = l1.position(l2)
        self.assertEqual(rp, on2d.Position.intersect)

        l1 = on2d.Line(a=0, b=1, c=-1)
        l2 = on2d.Line(a=0, b=-2, c=2)
        rp = l1.position(l2)
        self.assertEqual(rp, on2d.Position.match)

        l1 = on2d.Line(a=3, b=0, c=-1)
        l2 = on2d.Line(a=1, b=0, c=2)
        rp = l1.position(l2)
        self.assertEqual(rp, on2d.Position.parallel)

        with self.assertRaises(on2d.LineNotExists):
            on2d.Line(a=0, b=0, c=1)

    def test_angle(self):
        a = on3d.Point(x=2, y=0, z=-1)
        b = on3d.Point(x=0, y=0, z=0)
        c = on3d.Point(x=1, y=2, z=3)
        t_angle = on3d.Angle(a, b, c).type()
        self.assertEqual(t_angle, on3d.AngleType.Obtuse)

        a = on3d.Point(x=5, y=0, z=0)
        b = on3d.Point(x=0, y=0, z=0)
        c = on3d.Point(x=1, y=5, z=0)
        t_angle = on3d.Angle(a, b, c).type()
        self.assertEqual(t_angle, on3d.AngleType.Acute)

        a = on3d.Point(x=5, y=0, z=0)
        b = on3d.Point(x=0, y=0, z=0)
        c = on3d.Point(x=0, y=5, z=0)
        t_angle = on3d.Angle(a, b, c).type()
        self.assertEqual(t_angle, on3d.AngleType.Right)

        a = on3d.Point(x=5, y=0, z=0)
        b = on3d.Point(x=0, y=0, z=0)
        c = on3d.Point(x=-1, y=5, z=0)
        t_angle = on3d.Angle(a, b, c).type()
        self.assertEqual(t_angle, on3d.AngleType.Obtuse)

    def test_cross_product3d(self):
        a = on3d.Vector().from_coords(x=-1, y=2, z=-3)
        b = on3d.Vector().from_coords(x=0, y=-4, z=1)
        c = a.cross(b)
        # print(a, b, c, sep='\n')
        t1 = a.dot(c)
        t2 = b.dot(c)
        # print(t1, t2)

    def test_1(self):
        a = on3d.Point()
        b = on3d.Point(x=10)
        c = on3d.Point(x=4)
        d = on3d.Point(x=4, y=1)
        ab = on3d.Vector(a, b)
        ac = on3d.Vector(a, c)
        ad = on3d.Vector(a, d)
        print(ab.len())
        print(ab.cross(ac).len())
        print(ab.cross(ad).len())


unittest.main()