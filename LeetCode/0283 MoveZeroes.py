# https://leetcode.com/problems/move-zeroes/
# Runtime: 40 ms, faster than 97.90% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.4 MB, less than 16.24% of Python3 online submissions for Move Zeroes.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        not_0_point = []
        for num in nums:
            if num != 0:
                not_0_point.append(num)
        for i, num in enumerate(not_0_point):
            nums[i] = num
        for i in range(len(not_0_point), len(nums)):
            nums[i] = 0
