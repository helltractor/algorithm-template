for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(n - 1)
    idx = -1
    for i in reversed(range(n)):
        if a[i] % 2 == a[0] % 2:
            if idx < 0:
                idx = i
            else:
                print(i + 1, idx + 1)
    for i, x in enumerate(a):
        if x % 2 != a[0] % 2:
            print(1, i + 1)
