# https://leetcode.com/problems/knight-dialer/
# Runtime: 1180 ms, faster than 58.70% of Python3 online submissions for Knight Dialer.
# Memory Usage: 14.3 MB, less than 89.96% of Python3 online submissions for Knight Dialer.

class Solution:
    def knightDialer(self, n: int) -> int:
        from copy import copy
        MOD = 10**9+7
        pos = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9],
               6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        dp = [1]*10
        if n == 1:
            return 10
        for _ in range(1, n):
            dp_next = [0]*10
            for key, vals in pos.items():
                for val in vals:
                    dp_next[val] += dp[key]
            dp = copy(dp_next)
        return sum(dp) % MOD
