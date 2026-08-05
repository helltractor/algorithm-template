for _ in range(int(input())):
    n, x = map(int, input().split())
    if x == 0:
        if n % 2:
            if n < 3:
                print(-1)
            else:
                print(n + 3)
        else:
            print(n)
        continue
    if x == 1:
        if n % 2:
            print(n)
        else:
            print(n + 3)
        continue
    cnt = x.bit_count()
    m = n - min(n, cnt)
    if m == 0:
        print(x)
    else:
        print(x + m + m % 2)
