# https://leetcode.com/problems/shortest-common-supersequence/
# Runtime: 414 ms, faster than 98.56% of Python3 online submissions for Shortest Common Supersequence .
# Memory Usage: 22.8 MB, less than 60.81% of Python3 online submissions for Shortest Common Supersequence .


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Length of LCS
        m = len(str1)
        n = len(str2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Print LCS
        i = m
        j = n
        lcs = ""
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                lcs = lcs + str1[i - 1]
                i -= 1
                j -= 1
            else:
                if dp[i][j - 1] > dp[i - 1][j]:
                    j -= 1
                else:
                    i -= 1
        lcs = lcs[::-1]

        # Print Shortest Common Subsequence
        i = 0
        j = 0
        ans = ""
        for k in lcs:
            while str1[i] != k:
                ans = ans + str1[i]
                i += 1
            while str2[j] != k:
                ans = ans + str2[j]
                j += 1
            ans = ans + k
            i += 1
            j += 1
        return ans + str1[i:] + str2[j:]
