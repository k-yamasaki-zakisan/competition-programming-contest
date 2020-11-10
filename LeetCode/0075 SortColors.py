# https://leetcode.com/problems/sort-colors/
# Runtime: 36 ms, faster than 32.58% of Python3 online submissions for Sort Colors.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Sort Colors.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for all idx < p0: nums[idx < po] = 0
        # curr is an index of element under consideration
        p0 = curr = 0
        p2 = len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1