from sortedcontainers import SortedList

n = int(input())
s = list(input())
pre = 0
ans = 0
sl = SortedList([0])
for c in s:
    if c == "A":
        pre += 1
    elif c == "B":
        pre -= 1
    cur = sl.bisect_left(pre)
    ans += cur
    sl.add(pre)
print(ans)
