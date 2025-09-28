from struct.fenwick.template import FenwickTree
from util.io.fast_io import II, LI


class Solution:

    def cf2121g():
        """
        link: https://codeforces.com/problemset/problem/2121/G
        tag: fenwick tree | prefix sum | greedy
        """
        for _ in range(II()):
            n = II()
            a = LI()

            size = 2 * n + 1
            offset = n
            f = FenwickTree(size)

            zero = offset
            ans = 0
            s = 0
            for c in a:
                s += 1
                if c == "0":
                    s += f.range_query(zero, size - 1)
                    f.update(zero, 1)
                    zero -= 1
                else:
                    s += f.range_query(0, zero)
                    f.update(zero, 1)
                    zero += 1
                ans += s
            print(ans)
