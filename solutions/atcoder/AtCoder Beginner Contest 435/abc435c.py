n = int(input())
a = list(map(int, input().split()))
ans = 1
cur = a[0] - 1
for i in range(1, n):
    if cur >= i:
        cur = max(cur, i + a[i] - 1)
        ans += 1
print(ans)
