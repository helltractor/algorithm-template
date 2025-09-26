# Segment Tree

## 基本性质

线段树需要满足的性质：

- 运算满足结合律，即`(a·b)·c=a·(b·c)`；
- 存在单位元 e，即`a·e=e·a=a`。

因此对满足上述性质的元素类型 S，只要规定了二元运算 op 和单位元 e，就可以定义线段树的基本操作。

区间更新线段树 LazySegTree 比单点更新线段树 SegTree 多了懒标记以及懒标记上的操作。这就使得定义线段树基本操作时，除了元素类型 S、二元运算 op 和单位元 e 以外，还要定义区间修改的映射函数 mapping、映射函数的积 composition、以及映射不动点 id。简而言之：

- `mapping`：定义区间修改的方式；
- `composition`：定义区间上多个修改叠加的方式；
- `id`：表示不进行区间修改的懒标记。

## 参考

- [分享｜ AtCoder 线段树模板解读](https://leetcode.cn/discuss/post/3587109/atcoderxian-duan-shu-mo-ban-jie-du-by-fa-fp9j/)
