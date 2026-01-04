n = int(input())
a = list(map(int, input().split()))
f = [0] * (2 * n + 1)
for i, x in enumerate(a):
    f[i + n] = 1
    for j in range(i):
        if a[j] > x:
            f[i] = max(f[i], f[j + n] + 1)
        elif a[j] < x:
            f[i + n] = max(f[i + n], f[j] + 1)
print(max(f))
