# https://leetcode.com/problems/monotonic-array/
# Runtime: 1048 ms, faster than 7.99% of Python3 online submissions for Monotonic Array.
# Memory Usage: 28.6 MB, less than 25.32% of Python3 online submissions for Monotonic Array.

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_decr = is_incr = True

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                is_decr = False
            elif nums[i] > nums[i + 1]:
                is_incr = False

        return is_incr or is_decr
