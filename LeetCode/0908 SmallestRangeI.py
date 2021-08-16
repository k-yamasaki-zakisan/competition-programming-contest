# https://leetcode.com/problems/smallest-range-i/
# Runtime: 108 ms, faster than 86.03% of Python3 online submissions for Smallest Range I.
# Memory Usage: 15.4 MB, less than 8.98% of Python3 online submissions for Smallest Range I.

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(max(nums)-min(nums)-(2*k), 0)
