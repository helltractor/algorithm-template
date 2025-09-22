# Sparse Table

稀疏表（Sparse Table，ST 表）是一种静态区间查询的数据结构。能够在 O(1)时间内回答区间最值查询（RMQ，Range Minimum/Maximum Query），并且不支持修改。

稀疏表利用了**区间可分性**：
$$RMQ(L, R) = min(RMQ(L, M), RMQ(M+1, R))$$
其中 M 是区间中点，可以将任意区间划分为俩个长度为 2^k 的子区间。

## 预处理

假设原数组为 `a[0...n-1]`，构造表 `st[i][k]`，表示区间`[i, i+2^k-1]`的最值。

**递推公式：**
$$st[i][k]=min(st[i][k−1],st[i+2k−1][k−1])$$

**复杂度：**
总共`O(nlogn)`个状态，每个状态`O(1)`转移，所以总复杂度`O(nlogn)`。

## 查询

假设查询区间`[L, R]`，可覆盖两个长度为 2^k 的子区间。k 的计算如下：
$$k=⌊log_2(R-L+1)⌋$$

**递推公式：**
$$RMQ(L,R)=min(st[L][k],st[R−2k+1][k])$$

**复杂度：**
查询复杂度为`O(1)`。

## 示例代码

```python
def op(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return min(a[0], b[0]), max(a[1], b[1])


class ST:
    def __init__(self, a: List[int]):
        n = len(a)
        sz = n.bit_length()
        st = [[None] * sz for _ in range(n)]
        for i, x in enumerate(a):
            st[i][0] = (x, x)
        for j in range(1, sz):
            for i in range(n - (1 << j) + 1):
                st[i][j] = op(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
        self.st = st

    # [l, r) 左闭右开
    def query(self, l: int, r: int) -> int:
        k = (r - l).bit_length() - 1
        mn, mx = op(self.st[l][k], self.st[r - (1 << k)][k])
        return mx - mn
```
