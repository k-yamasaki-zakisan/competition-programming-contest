# https://leetcode.com/problems/minimum-cost-to-merge-stones/
# Runtime: 118 ms, faster than 33.80% of Python3 online submissions for Minimum Cost to Merge Stones.
# Memory Usage: 15.3 MB, less than 13.69% of Python3 online submissions for Minimum Cost to Merge Stones.

from typing import List


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
