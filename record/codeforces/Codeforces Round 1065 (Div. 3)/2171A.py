for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(n // 2 + 1):
        if (n - 2 * i) % 4 == 0:
            ans += 1
    print(ans)
