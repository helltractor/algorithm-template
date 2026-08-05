for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    st = n
    l = 0
    for i in range(n):
        if a[i] == st:
            st -= 1
        else:
            l = i
            break
    if st:
        r = a.index(st)
        a[l : r + 1] = reversed(a[l : r + 1])
    print(" ".join(map(str, a)))
