from typing import List
from math.xor_basis.template import XorBasis


class Solution:
    def lc_3681(self, nums: List[int]) -> int:
        """
        link: https://leetcode.cn/problems/maximum-xor-of-subsequences/
        """
        m = max(nums).bit_length()
        b = XorBasis(m)
        for x in nums:
            b.insert(x)
        return b.max_xor()
