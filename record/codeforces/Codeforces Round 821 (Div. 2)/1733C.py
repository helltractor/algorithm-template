for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if a == sorted(a):
        print(0)
        continue

    def cal(i, j):
        x, y = a[i], a[j]
        if x % 2 == y % 2:
            a[i] = y
        else:
            a[j] = x

    ans = [(1, n)]
    cal(0, n - 1)
    for i in range(1, n - 1):
        if a[0] % 2 != a[i] % 2:
            ans.append((1, i + 1))
        else:
            ans.append((i + 1, n))
    print(len(ans))
    for x, y in ans:
        print(x, y)
