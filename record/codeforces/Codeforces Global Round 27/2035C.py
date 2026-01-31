for _ in range(int(input())):
    n = int(input())
    if n % 2:
        ans = [n, n - 1, 3, 1, 2]
        for i in range(4, n - 1):
            ans.append(i)
        print(n)
        print(*ans[::-1])
    else:
        bit = n.bit_length() - 1
        ans = [1 << bit, (1 << bit) - 1, (1 << bit) - 2, 5, 1]
        st = set(ans)
        for i in range(1, n + 1):
            if i not in st:
                ans.append(i)
        print((1 << (bit + 1)) - 1)
        print(*ans[::-1])
