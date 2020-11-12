# https://leetcode.com/problems/unique-binary-search-trees/
# Runtime: 32 ms, faster than 42.26% of Python3 online submissions for Unique Binary Search Trees.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Unique Binary Search Trees.

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[-1]