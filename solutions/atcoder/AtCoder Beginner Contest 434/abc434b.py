n, m = map(int, input().split())
cnt = [0] * (m + 1)
s = [0] * (m + 1)
for _ in range(n):
    x, y = map(int, input().split())
    cnt[x] += 1
    s[x] += y
for x, y in zip(cnt[1:], s[1:]):
    print(y / x)
