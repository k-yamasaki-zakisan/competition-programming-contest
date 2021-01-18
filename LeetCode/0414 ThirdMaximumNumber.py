# https://leetcode.com/problems/third-maximum-number/
# Runtime: 40 ms, faster than 99.18% of Python3 online submissions for Third Maximum Number.
# Memory Usage: 15.6 MB, less than 45.61% of Python3 online submissions for Third Maximum Number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        if 2 < len(nums):
            return nums[2]
        else:
            return nums[0]
