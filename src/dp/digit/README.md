# Digit Dynamic Programing

## 单边界数位 dp 模板 (v1.0)

mask 表示前面选过的数字集合，换句话说，第 i 位要选的数字不能在 mask 中。

isLimit 表示当前是否受到了 n 的约束（注意要构造的数字不能超过 n）。若为真，则第 i 位填入的数字至多为 s[i]，否则可以是 9。如果在受到约束的情况下填了 s[i]，那么后续填入的数字仍会受到 n 的约束。例如 n=123，那么 i=0 填的是 1 的话，i=1 的这一位至多填 2。

isNum 表示 i 前面的数位是否填了数字。若为假，则当前位可以跳过（不填数字），或者要填入的数字至少为 1；若为真，则要填入的数字可以从 0 开始。例如 n=123，在 i=0 时跳过的话，相当于后面要构造的是一个 99 以内的数字了，如果 i=1 不跳过，那么相当于构造一个 10 到 99 的两位数，如果 i=1 跳过，相当于构造的是一个 9 以内的数字

> Author : 灵茶山艾府
> Link : https://leetcode.cn/problems/numbers-with-repeated-digits/solutions/1748539/by-endlesscheng-c5vg/

## 上下边界数位 dp 模板 (v2.0)

limitHigh 表示当前是否受到了 finish 的约束（我们要构造的数字不能超过 finish。若为真，则第 iii 位填入的数字至多为 finish[i]，否则至多为 9，这个数记作 hi。如果在受到约束的情况下填了 finish[i]，那么后续填入的数字仍会受到 finish 的约束。例如 finish=123，那么 i=0 填的是 1 的话，i=1 的这一位至多填 2。

limitLow 表示当前是否受到了 start 的约束（我们要构造的数字不能低于 start。若为真，则第 i 位填入的数字至少为 start[i]，否则至少为 0，这个数记作 lo。
如果在受到约束的情况下填了 start[i]，那么后续填入的数字仍会受到 start 的约束。

> Author : 灵茶山艾府
> Link : https://leetcode.cn/problems/count-the-number-of-powerful-integers/solutions/2595149/shu-wei-dp-shang-xia-jie-mo-ban-fu-ti-da-h6ci

```python
@lru_cache(None)
def dfs(i: int, limit_low: bool, limit_high: bool, is_num: bool) -> int:
    if i == len(high):
        return int(is_num)
    res = 0

    if i < diff and not is_num:  # 可以跳过当前数位
        res += dfs(i + 1, True, False, False)

    # 第 i 个数位可以从 lo 枚举到 hi
    # 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
    lo = low[i] if limit_low else 0
    hi = high[i] if limit_high else 9

    for d in range(max(lo, 1 - is_num), hi + 1):  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
        res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi, True)
    return res
```
