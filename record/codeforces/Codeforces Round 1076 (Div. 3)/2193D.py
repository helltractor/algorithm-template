import bisect


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()

    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + b[i]
    ans = 0
    for i, x in enumerate(a):
        idx = bisect.bisect_left(pre, n - i)
        if pre[idx] > n - i:
            idx -= 1
        ans = max(ans, x * idx)
    print(ans)
