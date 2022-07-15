# https://leetcode.com/problems/squares-of-a-sorted-array/
# Runtime: 333 ms, faster than 55.67% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 16.3 MB, less than 49.26% of Python3 online submissions for Squares of a Sorted Array.

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [num**2 for num in nums]
        ans.sort()
        return ans
