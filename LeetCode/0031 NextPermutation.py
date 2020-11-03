# https://leetcode.com/problems/next-permutation/
# Runtime: 36 ms, faster than 90.53% of Python3 online submissions for Next Permutation.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Next Permutation.

class Solution:
    def nextPermutation(self, nums: list) -> None:
        i = j = len(nums)-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i > 0:
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = reversed(nums[i:])
        return nums