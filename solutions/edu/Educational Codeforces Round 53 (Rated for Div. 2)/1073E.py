from functools import lru_cache


def count_numbers_in_range(low: int, high: int) -> int:
    low = list(map(int, str(low)))
    high = list(map(int, str(high)))
    n = len(high)
    diff = n - len(low)

    @lru_cache(None)
    def dfs(i: int, limit_low: bool, limit_high: bool, msk: int) -> int:
        if i == n:
            return [1, 0]

        res = [0, 0]
        lo = low[i - diff] if limit_low and i >= diff else 0
        hi = high[i] if limit_high else 9
        for d in range(lo, hi + 1):
            nmsk = msk | (1 << d)
            if nmsk.bit_count() > k:
                continue
            if msk == 0 and d == 0:
                tmp = dfs(i + 1, True, False, 0)
            else:
                tmp = dfs(i + 1, limit_low and d == lo, limit_high and d == hi, nmsk)
            res[0] = (res[0] + tmp[0]) % MOD
            res[1] = (res[1] + tmp[1] + pow(10, n - i - 1, MOD) * tmp[0] * d) % MOD
        return res

    ans = dfs(0, True, True, 0)[1]
    dfs.cache_clear()
    return ans


MOD = 998244353
l, r, k = map(int, input().split())
print(count_numbers_in_range(l, r))
