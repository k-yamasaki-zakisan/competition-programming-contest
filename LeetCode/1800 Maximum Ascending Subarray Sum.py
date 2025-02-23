from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = tmp = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                tmp += nums[i]
            else:
                tmp = nums[i]
            ans = max(ans, tmp)
        return ans
