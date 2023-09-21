from typing import List
from heapq import heappop, heappush


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0] * (n + 10)
        events = []
        offers.sort()
        for s, t, g in offers:
            heappush(events, [t, s, g])
        for i in range(len(dp)):
            dp[i] = dp[i - 1]
            while events and events[0][0] == i:
                t, s, g = heappop(events)
                dp[i] = max(dp[i], dp[s - 1] + g)
        return max(dp)
