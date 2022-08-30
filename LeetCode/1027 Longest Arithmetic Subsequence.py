# https://leetcode.com/problems/longest-arithmetic-subsequence/
# Runtime: 4206 ms, faster than 79.97% of Python3 online submissions for Longest Arithmetic Subsequence.
# Memory Usage: 97.6 MB, less than 9.56% of Python3 online submissions for Longest Arithmetic Subsequence.

from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        len_nums = len(nums)
        dp = {}
        for left in range(len_nums - 1):
            for right in range(left + 1, len_nums):
                diff = nums[right] - nums[left]
                dp[(diff, right)] = dp[(diff, left)] + 1 if (diff, left) in dp else 2
        return max(dp.values())
