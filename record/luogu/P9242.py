n = int(input())
a = list(map(int, input().split()))
f = [[0] * 10 for _ in range(10)]
for x in a:
    suf = x % 10
    pre = int(str(x)[0])
    nf = [row[:] for row in f]
    for y in range(10):
        nf[pre][suf] = max(nf[pre][suf], f[y][pre] + 1)
    f = nf
print(n - max(max(row) for row in f))
