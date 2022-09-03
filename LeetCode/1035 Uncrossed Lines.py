# https://leetcode.com/problems/uncrossed-lines/
# Runtime: 281 ms, faster than 73.83% of Python3 online submissions for Uncrossed Lines.
# Memory Usage: 14.2 MB, less than 67.83% of Python3 online submissions for Uncrossed Lines.

from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        len_1, len_2 = len(nums1), len(nums2)
        dp = [[0] * (len_2 + 1) for _ in range(len_1 + 1)]
        for i in range(1, len_1 + 1):
            for j in range(1, len_2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]
