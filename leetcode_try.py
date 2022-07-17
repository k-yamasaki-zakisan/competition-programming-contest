from typing import List

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        NEXT = (0, 6, 29)
        set_days = set(days)
        max_day = 450
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


days = [1, 4, 6, 7, 8, 20]
costs = [7, 2, 15]
S = Solution()
print(S.mincostTickets(days, costs))
