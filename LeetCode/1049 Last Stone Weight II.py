# https://leetcode.com/problems/last-stone-weight-ii/
# Runtime: 44 ms, faster than 97.48% of Python3 online submissions for Last Stone Weight II.
# Memory Usage: 13.9 MB, less than 88.36% of Python3 online submissions for Last Stone Weight II.

from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_num = sum(stones)
        dp = [0] * (sum_num // 2 + 1)
        dp[0] = 1
        diff = 0
        for stone in stones:
            for j in range(sum_num // 2, stone - 1, -1):
                if dp[j - stone]:
                    dp[j] = 1
                    diff = max(diff, j)
        return sum_num - 2 * diff
