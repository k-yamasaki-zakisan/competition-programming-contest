# https://leetcode.com/problems/maximum-of-absolute-value-expression/
# Runtime: 636 ms, faster than 48.61% of Python3 online submissions for Maximum of Absolute Value Expression.
# Memory Usage: 22.1 MB, less than 64.58% of Python3 online submissions for Maximum of Absolute Value Expression.

from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans, N = -float("inf"), len(arr1)
        for p, q in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            small_tmp = p * arr1[0] + q * arr2[0]
            for i in range(1, N):
                num = p * arr1[i] + q * arr2[i] + i
                ans = max(ans, num - small_tmp)
                small_tmp = min(small_tmp, num)
        return ans
