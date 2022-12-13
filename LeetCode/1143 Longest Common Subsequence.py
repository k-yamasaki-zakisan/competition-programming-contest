# https://leetcode.com/problems/longest-common-subsequence/description/


class Solution:
    def longestCommonSubsequence(self, T: str, S: str) -> int:
        len_T, len_S = len(T), len(S)
        dp = [[0] * (len_T + 1) for _ in range(len_S + 1)]
        for i in range(1, len_S + 1):
            for j in range(1, len_T + 1):
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]
