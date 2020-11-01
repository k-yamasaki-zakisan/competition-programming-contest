# https://leetcode.com/problems/remove-element/
# Runtime: 24 ms, faster than 97.62% of Python3 online submissions for Remove Element.
# Memory Usage: 14.1 MB, less than 99.98% of Python3 online submissions for Remove Element.

class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


# Runtime: 36 ms, faster than 33.33% of Python3 online submissions for Remove Element.
# Memory Usage: 14.1 MB, less than 99.98% of Python3 online submissions for Remove Element.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i