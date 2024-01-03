class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]

        for h in range(m):
            for w in range(n):
                if h == 0 or w == 0:
                    memo[h][w] = 1
                    continue
                memo[h][w] = memo[h - 1][w] + memo[h][w - 1]

        return memo[-1][-1]
