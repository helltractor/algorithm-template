n = int(input())
a = list(map(int, input().split()))
g = [[] for _ in range(n)]
degree = [0] * n
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    degree[u] += 1
    degree[v] += 1
    g[u].append(v)
    g[v].append(u)

ans = 0
if n > 1:
    st = set()
    q = []
    for i, d in enumerate(degree):
        if d == 1 and a[i] == 0:
            q.append(i)
    while q:
        nq = []
        for u in q:
            for v in g[u]:
                if degree[v]:
                    degree[v] -= 1
                    if degree[v] == 1 and a[v] == 0:
                        nq.append(v)
            degree[u] -= 1
            st.add(u)
        q = nq
    for i in range(n):
        if i not in st:
            if a[i] == 0:
                ans += 1
print(ans)
