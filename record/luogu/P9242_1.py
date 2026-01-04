n = int(input())
a = list(map(int, input().split()))
f = [0] * 10
for x in a:
    suf = x % 10
    pre = int(str(x)[0])
    f[suf] = max(f[suf], f[pre] + 1)
print(n - max(f))
