from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        from collections import defaultdict

        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        edges_key = defaultdict(list)
        dp = [[0] * (1 << n) for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    edges_key[i].append(j)
                    edges_key[j].append(i)

        for i in range(n):
            dp[i][1 << i] = 1

        for mask in range(1, 1 << n):
            for i in range(n):
                if mask & (1 << i):
                    for j in edges_key[i]:
                        if mask & (1 << j) == 0:
                            dp[j][mask | (1 << j)] += dp[i][mask]
                            dp[j][mask | (1 << j)] %= MOD

        return sum(dp[i][(1 << n) - 1] for i in range(n)) % MOD
