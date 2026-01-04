for _ in range(int(input())):
    l, r = map(int, input().split())
    factor = [2, 3, 5, 7]

    def cal(x):
        ans = x
        for i in range(1, 1 << 4):
            base = 1
            for j, y in enumerate(factor):
                if i >> j & 1:
                    base *= y
            if i.bit_count() % 2:
                ans -= x // base
            else:
                ans += x // base
        return ans

    print(cal(r) - cal(l - 1))
