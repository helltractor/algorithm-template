for _ in range(int(input())):
    n = int(input())
    vis = [False] * (n + 1)
    a = [1]
    b = []
    i = 2
    while i <= n:
        if not vis[i]:
            j = 1
            tmp = []
            while i * j <= n:
                if not vis[i * j]:
                    tmp.append(i * j)
                    vis[i * j] = True
                j += 1
            if i == 2 or i == 3:
                b.extend(tmp)
            else:
                a.extend(tmp)
        i += 1
    ans = []
    for i in range(len(a)):
        ans.append(a[i])
        if 2 * i < len(b):
            ans.append(b[i << 1])
        if 2 * i + 1 < len(b):
            ans.append(b[i << 1 | 1])
    ans.extend(b[len(a) << 1 :])
    print(*ans)
