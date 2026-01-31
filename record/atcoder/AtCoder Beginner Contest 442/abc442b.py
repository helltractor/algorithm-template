n = int(input())
a = [int(input()) for _ in range(n)]
cur = 0
flag = False
for x in a:
    if x == 1:
        cur += 1
    elif x == 2:
        if cur:
            cur -= 1
    else:
        flag = not flag
    print("Yes" if flag and cur >= 3 else "No")
