for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(n):
        for j in range(n):
            cur = i * n + j + 1
            res = cur
            if j:
                res += cur - 1
            if j + 1 < n:
                res += cur + 1
            if i:
                res += cur - n
            if i + 1 < n:
                res += cur + n
            ans = max(ans, res)
    print(ans)
