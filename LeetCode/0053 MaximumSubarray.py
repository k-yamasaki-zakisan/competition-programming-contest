# 
# Runtime: 64 ms, faster than 71.75% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.9 MB, less than 91.95% of Python3 online submissions for Maximum Subarray.

class Solution:
    def maxSubArray(self, nums: list) -> int:
        ans = nums[0]
        tmp = 0
        head = 0
        for i in range(len(nums)):
            tmp += nums[i]
            ans = max(ans,tmp)
            if tmp<0:
                while tmp<0:
                    tmp -= nums[head]
                    head += 1
        return ans