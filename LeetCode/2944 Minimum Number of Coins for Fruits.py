from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        INF = float("inf")
        n = len(prices)
        dp = [INF] * n
        dp[0] = prices[0]
        for i in range(1, n):
            for j in range(i):
                if i <= (j + 1) * 2:
                    dp[i] = min(dp[i], dp[j] + prices[i])

        return min([dp[i] for i in range(n) if n <= (i + 1) * 2])
