for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = [n] * k
    if k % 2 == 0:
        free = 0
        for i in reversed(range(n.bit_length())):
            if n >> i & 1:
                ans[min(free, k - 1)] ^= 1 << i
                free += 1
            else:
                for j in range(min(free - free % 2, k)):
                    ans[j] |= 1 << i
    print(*ans)
