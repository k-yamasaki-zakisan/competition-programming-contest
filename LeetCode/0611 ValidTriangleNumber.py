# https://leetcode.com/problems/valid-triangle-number/
# Runtime: 548 ms, faster than 28.81% of Python3 online submissions for Valid Triangle Number.
# Memory Usage: 14.2 MB, less than 86.06% of Python3 online submissions for Valid Triangle Number.

class Solution:
    def triangleNumber(self, nums: list) -> int:
        from bisect import bisect_left
        nums.sort()
        nums_len = len(nums)
        ans = 0
        for i in range(nums_len-2):
            for j in range(i+1, nums_len-1):
                target_hen = nums[i]+nums[j]
                target_i = bisect_left(nums, target_hen)
                if j < target_i:
                    ans += target_i-j-1
        return ans
