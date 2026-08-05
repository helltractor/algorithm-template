n, med = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * (n + 1)
d = {}
ans = 0
idx = a.index(med)
for i in range(n):
    cnt[i + 1] = cnt[i] + int(a[i] > med) - int(a[i] < med)
for i in range(n):
    if i <= idx:
        d[cnt[i]] = d.get(cnt[i], 0) + 1
    if i >= idx:
        ans += d.get(cnt[i + 1], 0)
print(ans)
