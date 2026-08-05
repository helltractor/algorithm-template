for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = [10**18] * (n + 1)
    for x in a:
        f[x] = min(f[x], 1)
    for i in range(1, n + 1):
        if f[i] == 10**18:
            continue
        j = 1
        while i * j <= n:
            k = i * j
            f[k] = min(f[k], f[i] + f[j])
            j += 1
    for i, x in enumerate(f):
        if x == 10**18:
            f[i] = -1
    print(" ".join(map(str, f[1:])))
