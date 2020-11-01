# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Runtime: 88 ms, faster than 49.58% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.6 MB, less than 89.72% of Python3 online submissions for Remove Duplicates from Sorted Array.

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i = 0
        while i+1 < len(nums):
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
        return len(nums)