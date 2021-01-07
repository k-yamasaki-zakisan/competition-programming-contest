# https://leetcode.com/problems/missing-number/
# Runtime: 132 ms, faster than 59.00% of Python3 online submissions for Missing Number.
# Memory Usage: 15.3 MB, less than 67.38% of Python3 online submissions for Missing Number.

class Solution:
    def missingNumber(self, nums: list) -> int:
        nums.sort()
        point = 0
        for i in range(len(nums)+1):
            if len(nums) == point:
                return i
            elif nums[point] == i:
                point += 1
            else:
                return i
