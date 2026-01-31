for _ in range(int(input())):
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))
    t = sum(a)
    print("YES" if t <= s and (s - t) % x == 0 else "NO")
