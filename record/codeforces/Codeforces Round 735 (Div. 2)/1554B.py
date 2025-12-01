fmax = lambda x, y: x if x > y else y
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    w = n.bit_length()
    f = [[0, 0] for _ in range(1 << w)]
    for i, x in enumerate(a, 1):
        f[x] = [i, f[x][0]]

    for i in range(w):
        bit = 1 << i
        for j in range(1 << w):
            if j >> i & 1:
                continue
            t, j = j, j | bit
            if f[j][0] < f[t][0]:
                f[j][1] = fmax(f[j][0], f[t][1])
                f[j][0] = f[t][0]
            elif f[j][1] < f[t][0]:
                f[j][1] = f[t][0]

    ans = -(10**10)
    for i, p in enumerate(f):
        if p[1] > 0:
            ans = fmax(ans, p[0] * p[1] - k * i)
    print(ans)
