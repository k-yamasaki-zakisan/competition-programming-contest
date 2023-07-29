from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        len_n = len(nums)
        memo = [0] * (len_n + 10)
        for num in nums:
            if 0 < num <= len_n + 5:
                memo[num] += 1
        for cand in range(1, len_n + 10):
            if memo[cand] == 0:
                return cand
        return len_n + 1
