# https://leetcode.com/problems/divisor-game/
# Runtime: 106 ms, faster than 14.51% of Python3 online submissions for Divisor Game.
# Memory Usage: 13.9 MB, less than 55.97% of Python3 online submissions for Divisor Game.


class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N + 1)
        for i in range(2, N + 1):
            for j in range(1, i):
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
                    break
        return dp[N]
