n = int(input())
a = list(map(int, input().split()))
MOD9 = 998244353
ans = 0
f = [[0] * 2 for _ in range(2)]
cnt = [0] * 2
for x in a:
    nf = [row[:] for row in f]
    for j in range(2):
        for k in range(2):
            if (j + k + x) % 2 == 0:
                nf[k][x % 2] = (nf[k][x % 2] + f[j][k]) % MOD9
                ans = (ans + f[j][k]) % MOD9
    for j in range(2):
        nf[j][x % 2] = (nf[j][x % 2] + cnt[j]) % MOD9
    cnt[x % 2] += 1
    f = nf
print(ans)
