from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        left_sum, right_sum = 0, sum(nums)
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if right_sum <= left_sum:
                ans += 1
        return ans
