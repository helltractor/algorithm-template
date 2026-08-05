#!/usr/bin/env python3


class Cmp:
    """
    极角排序，逆时针方向
    例如：key=cmp_to_key(lambda p1, p2: func(p1, p2))
    """

    @staticmethod
    def polar_angle_sorting(p1, p2):
        # 半平面
        half = lambda p: p[1] < 0 or (p[1] == 0 and p[0] < 0)
        h1, h2 = half(p1), half(p2)
        if h1 != h2:
            return -1 if h1 < h2 else 1
        # 叉积
        crossing = lambda a, b: a[0] * b[1] - a[1] * b[0]
        crossing_val = crossing(p1, p2)
        if crossing_val > 0:
            return -1
        elif crossing_val < 0:
            return 1
        return 0
