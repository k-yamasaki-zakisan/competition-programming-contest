from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        edges = [[0] * n for _ in range(n)]
        dp = [[0] * n for _ in range(1 << n)]

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    edges[i][j] = 1

        for i in range(n):
            dp[1 << i][i] = 1

        for mask in range(1, 1 << n):
            for i in range(n):
                if mask & (1 << i):
                    for j in range(n):
                        if (mask & (1 << j) == 0) and edges[i][j]:
                            dp[mask | (1 << j)][j] += dp[mask][i]
                            dp[mask | (1 << j)][j] %= MOD

        return sum(dp[(1 << n) - 1]) % MOD


S = Solution()

nums = [2, 3, 6]
print(S.specialPerm(nums))
