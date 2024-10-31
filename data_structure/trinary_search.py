# _*_ coding: utf-8 _*_
# @File : trinary_search.py
# @Time : 2024/8/7 上午1:46


def trinary_search(l: int, r: int, target: int, f: callable) -> int:
    while l <= r:
        ml = l + (r - l) // 3
        mr = r - (r - l) // 3
        if target < f(ml):
            r = ml - 1
        elif target > f(mr):
            l = mr + 1
        elif target != f(ml) and target != f(mr):
            l = ml + 1
            r = mr - 1
        else:
            return ml if target == f(ml) else mr
    return -1
