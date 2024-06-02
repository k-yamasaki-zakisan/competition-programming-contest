from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        ans = 0
        now = 1
        meetings.sort()
        print(meetings)
        for s, g in meetings:
            if now < s:
                ans += s - now - 1
            now = max(now, g)
            print(ans, now)
        if now < days:
            ans += days - now - 1
        return ans


S = Solution()
days = 10
meetings = [[5, 7], [1, 3], [9, 10]]
print(S.countDays(days, meetings))
# 10
