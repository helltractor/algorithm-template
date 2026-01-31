# Segment Tree

## 基本性质

线段树需要满足的性质：

- 运算满足结合律，即`(a·b)·c=a·(b·c)`；
- 存在单位元 e，即`a·e=e·a=a`。

因此对满足上述性质的元素类型 S，只要规定了二元运算 op 和单位元 e，就可以定义线段树的基本操作。

区间更新线段树 LazySegTree 比单点更新线段树 SegTree 多了懒标记以及懒标记上的操作。这就使得定义线段树基本操作时，除了元素类型 S、二元运算 op 和单位元 e 以外，还要定义区间修改的映射函数 mapping、映射函数的积 composition、以及映射不动点 id。简而言之：

- `mapping(f, x)`：定义区间修改的更新方式，f 表示懒标记，x 表示区间映射；
- `composition(f, g)`：定义懒标记的更新方式，f 表示新懒标记，g 表示旧懒标记；
- `id`：表示区间修改的懒标记。

## 模板解析

```python
class LazySegTree:
    def __init__(
            self,
            op: typing.Callable[[typing.Any, typing.Any], typing.Any],
            e: typing.Any,
            mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
            composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
            id_: typing.Any,
            v: typing.Union[int, typing.List[typing.Any]],
    ) -> None:
        self._op = op  # 线段树的合并操作，例如：max,add,gcd
        self._e = e  # 线段树的值的幺元，默认大小
        self._mapping = mapping  # 父结点的懒标记更新子结点的值，区间修改 F(映射) 的方法，定义 def mapping(x,y):
        self._composition = composition  # 父结点的懒标记更新子结点的懒标记，区间修改 F 的条件，定义 def composition(x,y): (懒标记相关）
        self._id = id_  # 更新操作/懒标记的幺元，恒等映射id(F作用于None得到的返回值)，例如：add的id_ = 0,max的id_ = -inf

        if isinstance(v, int):  # 原数组（如果输入int则表示数组长度，用幺元生成数组）
            v = [e] * v

        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)


    # 单点修改，修改a[p] = x，复杂度：o(logn)
    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    # 单点查询，返回a[p]，复杂度：o(1)
    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    # 区间查询，返回op(a[l],……,a[r-1])，复杂度：o(logn)
    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)

        sml = self._e
        smr = self._e
        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    # 返回op(a[0], ..., a[n - 1])，复杂度：o(1)
    def all_prod(self) -> typing.Any:
        return self._d[1]

    # 区间修改，
    def apply(
            self,
            left: int,
            right: typing.Optional[int] = None,
            f: typing.Optional[typing.Any] = None,
    ) -> None:
        assert f is not None

        if right is None:
            p = left
            assert 0 <= left < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    # 树上二分，返回一个r满足g(op(a[l],……,a[r-1])) == True，g(a[r]) == False
    # 树上二分查询最大的 `right` 使得切片 `[left:right]` 内的值满足 `key`
    def max_right(self, left: int, g: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    # 树上二分查询最小的 `left` 使得切片 `[left:right]` 内的值满足 `key`
    def min_left(self, right: int, g: typing.Any) -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: typing.Any) -> None:
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id
```

## 参考

- [分享｜ AtCoder 线段树模板解读](https://leetcode.cn/discuss/post/3587109/atcoderxian-duan-shu-mo-ban-jie-du-by-fa-fp9j/)
