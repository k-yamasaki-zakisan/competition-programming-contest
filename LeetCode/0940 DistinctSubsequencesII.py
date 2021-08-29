# https://leetcode.com/problems/distinct-subsequences-ii/
# Runtime: 52 ms, faster than 69.65% of Python3 online submissions for Distinct Subsequences II.
# Memory Usage: 14.5 MB, less than 21.10% of Python3 online submissions for Distinct Subsequences II.

class Solution:
    def distinctSubseqII(self, S: str) -> int:
        dp = [1]
        last = {}
        for i, s in enumerate(S):
            dp.append(dp[-1]*2)
            if s in last:
                dp[-1] -= dp[last[s]]
            last[s] = i
        return (dp[-1]-1) % (10**9+7)
