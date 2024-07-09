from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        leave_friends = set()
        now = 1
        for _ in range(n - 1):
            cnt = 0
            while cnt != k:
                if now not in leave_friends:
                    cnt += 1
                now += 1
                if n < now:
                    now -= n
            leave_friends.add(now)
            while now in leave_friends:
                now += 1
                if n < now:
                    now -= n
        now += 1
        if n < now:
            now -= n
        return now


S = Solution()
n = 5
k = 2
print(S.findTheWinner(n, k))
# 10
