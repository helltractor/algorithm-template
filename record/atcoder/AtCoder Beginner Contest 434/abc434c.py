for _ in range(int(input())):
    n, h = map(int, input().split())
    pre = 0
    mx = h
    mn = h
    flag = True
    for _ in range(n):
        t, l, u = map(int, input().split())
        mx = mx + (t - pre)
        mn = mn - (t - pre)
        if mn > u or mx < l:
            flag = False
        mx = min(mx, u)
        mn = max(mn, l)
        pre = t
    print("Yes" if flag else "No")
