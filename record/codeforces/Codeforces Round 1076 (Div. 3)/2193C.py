for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    qs = [list(map(int, input().split())) for _ in range(q)]

    for i in reversed(range(n)):
        if b[i] > a[i]:
            a[i] = b[i]
        if i + 1 < n and a[i + 1] > a[i]:
            a[i] = a[i + 1]

    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + a[i]
    ans = []
    for l, r in qs:
        ans.append(pre[r] - pre[l - 1])
    print(" ".join(map(str, ans)))
