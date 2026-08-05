#!/usr/bin/env python3

from typing import List
from collections import deque
from bisect import bisect_left


class Solution:

    def lc2071(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        """
        link: https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/
        """
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(k: int) -> bool:
            i, p = 0, pills
            q = deque()
            for w in workers[-k:]:
                while i < k and tasks[i] <= w + strength:
                    q.append(tasks[i])
                    i += 1
                if not q:
                    return False
                if w >= q[0]:  # 不嗑药能完成的任务
                    q.popleft()
                else:  # 嗑药能完成的最大任务
                    if p == 0:
                        return False
                    p -= 1
                    q.pop()
            return True

        left = ans = 0
        right = min(n, m)
        while left <= right:
            mid = (left + right + 1) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def lc2071_bisect(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        """
        link: https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/
        """
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(k: int) -> bool:
            k += 1
            i, p = 0, pills
            q = deque()
            for w in workers[-k:]:
                while i < k and tasks[i] <= w + strength:
                    q.append(tasks[i])
                    i += 1
                if not q:
                    return True
                if w >= q[0]:
                    q.popleft()
                else:
                    if p == 0:
                        return True
                    p -= 1
                    q.pop()
            return False

        return bisect_left(range(min(n, m)), True, key=check)
