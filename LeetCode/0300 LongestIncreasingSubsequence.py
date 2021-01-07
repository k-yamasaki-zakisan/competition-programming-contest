# https://leetcode.com/problems/longest-increasing-subsequence/
# Runtime: 60 ms, faster than 95.23% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.6 MB, less than 63.95% of Python3 online submissions for Longest Increasing Subsequence.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from bisect import bisect_left
        LIS = [nums[0]]
        for i in range(len(nums)):
            if nums[i] > LIS[-1]:
                LIS.append(nums[i])
            else:
                LIS[bisect_left(LIS, nums[i])] = nums[i]

        return len(LIS)
