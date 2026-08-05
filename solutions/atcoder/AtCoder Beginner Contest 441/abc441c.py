n, k, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if sum(a[:k]) < x:
    print(-1)
else:
    a = a[::-1]
    ans = n - k
    s = 0
    for i, y in enumerate(a[n - k :], 1):
        s += y
        if s >= x:
            ans += i
            break
    print(ans)
