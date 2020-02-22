from .on2d import Segment as Segment2D, Ray as Ray2D, Line as Line2D
from .on3d import Point as Point3D, Line as Line3D, Vector as Vector3D

def intersects(*, s: Segment2D, r: Ray2D):
    # TODO проверить что все точки лежат на одной прямой
    # s -> [a, b]
    # r -> [a, b)
    l_segment_x, r_segment_x =  min(s.a.x, s.b.x), max(s.a.x, s.b.x)
    if r.b.x >= r.a.x:
        # r ->
        return r_segment_x >= r.a.x
    else:
        # r <-
        return l_segment_x <= r.a.x

def on_once_line(a: Point3D, b: Point3D, c:Point3D):
    ab = Vector3D(a, b)
    ac = Vector3D(a, c)
    return ab.cross(ac).len() == 0

