from src.string.suffix_array.template import SuffixArray
from util.io.fast_io import II


class Solution:

    def nowcoder_271929():
        """
        link: https://ac.nowcoder.com/acm/problem/271929
        turorial: https://www.nowcoder.com/discuss/606190255179329536
        """
        s = II()
        n = len(s)
        suffix_array = SuffixArray(s)
        ans = n * (n + 1) // 2
        for i in range(1, n):
            ans -= suffix_array.height[i]
        print(ans)
