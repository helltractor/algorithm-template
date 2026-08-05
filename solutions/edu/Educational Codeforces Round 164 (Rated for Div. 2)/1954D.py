fmax = lambda x, y: x if x > y else y
n = int(input())
a = sorted(list(map(int, input().split())))
MOD9 = 998244353
ans = s = 0
f = [0] * 5001
f[0] = 1
for x in a:
    for y in range(s + 1):
        ans = (ans + f[y] * fmax((x + y + 1) // 2, x)) % MOD9
    for y in reversed(range(s + 1)):
        f[x + y] = (f[x + y] + f[y]) % MOD9
    s += x
print(ans)
