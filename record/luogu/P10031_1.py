for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        n ^= n // 2
    print(n)
