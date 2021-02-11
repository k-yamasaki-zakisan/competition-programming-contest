# https://leetcode.com/problems/maximum-average-subarray-i/
# Runtime: 832 ms, faster than 66.09% of Python3 online submissions for Maximum Average Subarray I.
# Memory Usage: 18.1 MB, less than 52.90% of Python3 online submissions for Maximum Average Subarray I.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp = sum(nums[:k])
        ans = tmp/k
        for i in range(k, len(nums)):
            tmp += nums[i]-nums[i-k]
            ans = max(tmp/k, ans)
        return ans
