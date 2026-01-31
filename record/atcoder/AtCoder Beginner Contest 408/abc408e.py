n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(m)]


def find(x):
    root = x
    while fa[root] != root:
        root = fa[root]
    while fa[x] != root:
        fa[x], x = root, fa[x]
    return root


ans = 0
for i in reversed(range(30)):
    fa = list(range(n + 1))
    target = ans >> i
    for u, v, w in g:
        if w >> i | target == target:
            fa[find(u)] = find(v)
    if find(1) != find(n):
        ans += 1 << i
print(ans)
