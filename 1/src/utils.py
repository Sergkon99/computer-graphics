from .on2d import Segment as Segment2D, Ray as Ray2D, Line as Line2D
from .on3d import Point as Point3D, Line as Line3D, Vector as Vector3D
from .exceptions import InputError

def intersects(*, s: Segment2D, r: Ray2D):
    line = Line2D().from_points(s.a, s.b)
    if not line.belongs(r.a) or not line.belongs(r.b):
        raise InputError('points do not belong to one line')
    # s -> [a, b]
    # r -> [a, b)
    l_segment_x, r_segment_x =  min(s.a.x, s.b.x), max(s.a.x, s.b.x)
    d_segment_y, u_segment_y = min(s.a.y, s.b.y), max(s.a.y, s.b.y)
    if l_segment_x - r_segment_x != 0:
        if r.b.x >= r.a.x:
            # r ->
            return r_segment_x >= r.a.x
        else:
            # r <-
            return l_segment_x <= r.a.x
    else:
        if r.b.y >= r.a.y:
            # up
            return u_segment_y >= r.a.y
        else:
            # down
            return d_segment_y <= r.a.y

def on_once_line(a: Point3D, b: Point3D, c:Point3D):
    ab = Vector3D(a, b)
    ac = Vector3D(a, c)
    return ab.cross(ac).len() == 0

