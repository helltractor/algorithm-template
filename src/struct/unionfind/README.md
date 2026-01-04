# 并查集（UnionFind）

## find 方法

### 递归实现

```python
def find(self, x: int) -> int:
    if self.fa[x] != x:
        self.fa[x] = self.find(self.fa[x])
    return self.fa[x]
```

### 非递归实现

**单循环路径压缩：**

```python
def find(self, x: int) -> int:
    while x != self.fa[x]:
        self.fa[x] = self.fa[self.fa[x]]
        x = self.fa[x]
    return x
```

**双循环路径压缩：**

```python
def find(self, x: int) -> int:
    root = x
    while root != self.fa[root]:
        root = self.fa[root]
    while x != root:
        x, self.fa[x] = self.fa[x], root
    return root
```

**带权并查集路径压缩：**

```python
def find(self, x: int) -> int:
    root, tot = x, 0
    while self.fa[root] != root:
        tot += self.dis[root]
        root = self.fa[root]

    while self.fa[x] != root:
        fa, tmp = self.fa[x], self.dis[x]
        self.dis[x] = tot
        tot -= tmp
        self.fa[x] = root
        x = fa
    return root
```
