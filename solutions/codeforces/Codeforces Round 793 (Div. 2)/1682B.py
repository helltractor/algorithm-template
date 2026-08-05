for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = -1
    for i in reversed(range(n)):
        if a[i] != i:
            ans &= a[i]
    print(ans)
