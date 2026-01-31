x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
if x1 <= x2 < x1 + 100 and y1 <= y2 < y1 + 100:
    print("Yes")
else:
    print("No")
