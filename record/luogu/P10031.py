from math import gcd

#gcd(i, n) == gcd(n-i, n)
for _ in range(int(input())):
    n = int(input())
    if n % 2:
        print(n)
    else:
        print(gcd(n, n // 2) ^ n)
