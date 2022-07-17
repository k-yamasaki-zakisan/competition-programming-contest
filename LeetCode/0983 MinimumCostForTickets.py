# https://leetcode.com/problems/minimum-cost-for-tickets/
# Runtime: 45 ms, faster than 93.76% of Python3 online submissions for Minimum Cost For Tickets.
# Memory Usage: 13.8 MB, less than 90.59% of Python3 online submissions for Minimum Cost For Tickets.

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        NEXT = (0, 6, 29)
        set_days = set(days)
        max_day = 400
        dp = [10**10] * max_day
        dp[0] = 0
        for i in range(1, max_day):
            if i in set_days:
                for j in range(3):
                    n = NEXT[j]
                    cost = costs[j]
                    if i + n < max_day:
                        dp[i + n] = min(dp[i + n], dp[i - 1] + cost)
            else:
                dp[i] = min(dp[i], dp[i - 1])
        return dp[-1]
