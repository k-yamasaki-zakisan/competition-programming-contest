# https://leetcode.com/problems/subarray-sum-equals-k/
# Runtime: 260 ms, faster than 56.53% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16.8 MB, less than 29.11% of Python3 online submissions for Subarray Sum Equals K.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        memo = defaultdict(int)
        memo[0] += 1
        tmp = ans = 0
        for num in nums:
            tmp += num
            if tmp-k in memo:
                ans += memo[tmp-k]
            memo[tmp] += 1
        return ans
