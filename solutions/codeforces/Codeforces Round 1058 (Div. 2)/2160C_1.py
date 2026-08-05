for _ in range(int(input())):
    n = int(input())
    s = bin(n)[2:].rstrip('0')
    print("YES" if s == s[::-1] and s.count("1") & 1 == 0 else "NO")
