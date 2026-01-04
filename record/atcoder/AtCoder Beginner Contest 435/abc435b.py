n = int(input())
a = list(map(int, input().split()))
ans = 0
pre = [0] * (n + 1)
for i in range(n):
    pre[i + 1] = pre[i] + a[i]

for l in range(n):
    for r in range(l + 1, n + 1):
        cur = pre[r] - pre[l]
        flag = True
        for i in range(l, r):
            if cur % a[i] == 0:
                flag = False
                break
        if flag:
            ans += 1
print(ans)
