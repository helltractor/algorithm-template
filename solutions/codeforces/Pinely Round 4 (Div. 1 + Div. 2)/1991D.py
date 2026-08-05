for _ in range(int(input())):
    n = int(input())
    a = [1, 2, 2, 3, 3]
    if n > 5:
        ans = [i % 4 + 1 for i in range(n)]
        print(4)
        print(*ans)
    else:
        print(n // 2 + 1)
        print(*a[:n])
