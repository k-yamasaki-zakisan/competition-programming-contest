# https://leetcode.com/problems/climbing-stairs/
# Runtime: 20 ms, faster than 98.29% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]