# https://leetcode.com/problems/delete-operation-for-two-strings/
# Runtime: 280 ms, faster than 71.98% of Python3 online submissions for Delete Operation for Two Strings.
# Memory Usage: 15.9 MB, less than 83.46% of Python3 online submissions for Delete Operation for Two Strings.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s = word1
        t = word2

        dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
