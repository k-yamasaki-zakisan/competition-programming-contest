from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        INF = float("inf")
        n = len(prices)
        dp = [INF] * n
        dp[0] = prices[0]
        for i in range(1, n):
            for j in range(i):
                if (j + 1) * 2 < i:
                    continue
                dp[i] = min(dp[i], dp[j] + prices[i])
        ans = INF
        for i in range(n):
            if (i + 1) * 2 < n:
                continue
            ans = min(ans, dp[i])
        return ans
