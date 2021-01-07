# https://leetcode.com/problems/perfect-squares/
# Runtime: 6008 ms, faster than 11.84% of Python3 online submissions for Perfect Squares.
# Memory Usage: 14.2 MB, less than 94.08% of Python3 online submissions for Perfect Squares.

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        for i in range(0, n+1):
            j = 1
            while i+j*j <= n:
                dp[i+j*j] = min(dp[i+j*j], dp[i]+1)
                j += 1
        return dp[n]
