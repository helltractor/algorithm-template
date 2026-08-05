for _ in range(int(input())):
    n = int(input())
    s = list(input())
    if n % 2:
        print(-1)
        continue
    a = list(map(lambda c: ord(c) - 97, s))
    tot = [0] * 26
    for i, x in enumerate(a):
        tot[x] += 1
    if max(tot) > n // 2:
        print(-1)
        continue
    mx = k = 0
    cnt = [0] * 26
    for i in range(n // 2):
        if a[i] == a[~i]:
            k += 1
            cnt[a[i]] += 1
            mx = max(mx, cnt[a[i]])
    print(max((k + 1) // 2, mx))
