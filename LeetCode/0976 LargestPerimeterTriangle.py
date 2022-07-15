# https://leetcode.com/problems/largest-perimeter-triangle/
# Runtime: 306 ms, faster than 46.30% of Python3 online submissions for Largest Perimeter Triangle.
# Memory Usage: 15.5 MB, less than 46.03% of Python3 online submissions for Largest Perimeter Triangle.

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        len_nums = len(nums)
        for i in range(len_nums - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]
            if a < b + c:
                return a + b + c
        return 0
