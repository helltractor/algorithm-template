for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    mx = 0
    b = []
    for x in a:
        if x == 0:
            continue
        b.append(x)
        s += 1
        if x > mx:
            mx = x
    if mx == n:
        print(s)
    else:
        t = sum(b) - len(b)
        if t >= n:
            print(len(b))
        else:
            print(len(b) - (n - t) + 1)
