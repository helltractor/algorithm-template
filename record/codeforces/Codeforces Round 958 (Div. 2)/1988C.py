for _ in range(int(input())):
    n = int(input())
    ans = [n]
    for i in range(n.bit_length()):
        if n >> i & 1:
            m = n ^ (1 << i)
            m |= n ^ ans[-1]
            if m:
                ans.append(m)
    print(len(ans))
    print(*ans[::-1])
