from typing import List

INF = 10**9


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [INF] * (last_day + 32)
        dp[0] = now = 0
        for i in range(1, last_day + 1):
            if days[now] == i:
                dp[i] = min(dp[i], dp[i - 1] + costs[0])
                dp[i + 6] = min(dp[i + 6], dp[i - 1] + costs[1])
                dp[i + 29] = min(dp[i + 29], dp[i - 1] + costs[2])
                now += 1
            else:
                dp[i] = min(dp[i], dp[i - 1])
        return min(dp[last_day:])
