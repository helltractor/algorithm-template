from math import gcd

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    g = 0
    for x in a:
        g = gcd(g, x)
    ans = a
    if g == 1:
        for i in range(n):
            ans[i] += a[i] % (k + 1) * k
    print(" ".join(map(str, ans)))
