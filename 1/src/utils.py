from .on2d import Segment, Ray, Line

def intersects(*, s: Segment, r: Ray):
    # TODO проверить что все точки лежат на одной прямой
    # s -> [a, b]
    # r -> [a, b)
    l_segment_x, r_segment_x =  min(s.a.x, s.b.x), max(s.a.x, s.b.x)
    if r.b.x >= r.a.x:
        # r ->
        if r_segment_x >= r.a.x:
            return True
        return False
    else:
        # r <-
        if l_segment_x <= r.a.x:
            return True
        return False

