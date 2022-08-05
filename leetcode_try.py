from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(l, r, pile):
            if pile == K and (r - l) % (pile - 1):
                return float("inf")
            if l == r:
                return 0
            if pile == 1:
                return dfs(l, r, K) + sum(stones[l : r + 1])
            return min(dfs(l, i, 1) + dfs(i + 1, r, pile - 1) for i in range(l, r))

        ans = dfs(0, len(stones) - 1, 1)
        return -1 if ans == float("inf") else ans


stones = [3, 5, 1, 2, 6]
k = 3
S = Solution()
print(S.mergeStones(stones, k))
