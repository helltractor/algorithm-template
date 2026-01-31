n, m, k = map(int, input().split())
mat = [list(map(int, input())) for _ in range(n)]
pre = [[0] * (n + 1) for _ in range(m)]
for i in range(m):
    for j in range(n):
        pre[i][j + 1] = pre[i][j] + mat[j][i]
ans = 10**9
for i in range(n):
    for j in range(n - 1, i - 1, -1):
        l = 0
        cur = 0
        for r in range(m):
            cur += pre[r][j + 1] - pre[r][i]
            if cur >= k:
                while cur >= k:
                    cur -= pre[l][j + 1] - pre[l][i]
                    l += 1
                ans = min(ans, (r - l + 2) * (j - i + 1))
print(ans if ans < 10**9 else 0)
