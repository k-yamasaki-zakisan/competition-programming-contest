# https://leetcode.com/problems/minimum-size-subarray-sum/
# Runtime: 76 ms, faster than 39.01% of Python3 online submissions for Minimum Size Subarray Sum.
# Memory Usage: 16.6 MB, less than 46.80% of Python3 online submissions for Minimum Size Subarray Sum.

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        tail = 0
        sum_point = 0
        ans = 10**10
        for head in range(len(nums)):
            sum_point += nums[head]
            if s <= sum_point:
                while s <= sum_point:
                    ans = min(ans, head-tail+1)
                    sum_point -= nums[tail]
                    tail += 1
        if ans == 10**10:
            return 0
        else:
            return ans