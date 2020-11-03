# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Runtime: 36 ms, faster than 88.61% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.5 MB, less than 15.15% of Python3 online submissions for Search in Rotated Sorted Array.

class Solution:
    def search(self, nums: list, target: int) -> int:
        try:
            ans = nums.index(target)
            return ans
        except:
            return -1