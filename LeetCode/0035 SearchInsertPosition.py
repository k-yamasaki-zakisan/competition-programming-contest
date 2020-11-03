# https://leetcode.com/problems/search-insert-position/
# Runtime: 48 ms, faster than 69.31% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.6 MB, less than 79.69% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        from bisect import bisect_left
        return bisect_left(nums, target)


# Runtime: 48 ms, faster than 69.31% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.7 MB, less than 79.69% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        nums.append(10**10)
        left = 0
        right = len(nums)-1
        while 1 < right-left:
            mid = (right+left)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid
        if target <= nums[left]:
            return left
        else:
            return right