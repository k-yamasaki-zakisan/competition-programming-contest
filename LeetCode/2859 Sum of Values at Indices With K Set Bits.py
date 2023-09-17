from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        len_nums = len(nums)
        ans = 0
        for i in range(len_nums):
            bin_i = bin(i)[2:]
            count_k = bin_i.count("1")
            if count_k == k:
                ans += nums[i]
        return ans
