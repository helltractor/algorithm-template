n, q = map(int, input().split())
a = list(map(int, input().split()))
qs = [int(input()) for _ in range(q)]

for k in qs:
    b = a[:]
    ans = 0
    for i in reversed(range(20)):
        s = 0
        for x in b:
            if x >> i & 1: continue
            y = (x >> i << i) + (1 << i)
            y += ans ^ (ans & y)
            s += y - x
            if s > k:
                break
        if s > k:
            continue
        for j, x in enumerate(b):
            if x >> i & 1: continue
            y = (x >> i << i) + (1 << i)
            y += ans ^ (ans & y)
            b[j] = y
        ans += 1 << i
        k -= s
    print(ans)
