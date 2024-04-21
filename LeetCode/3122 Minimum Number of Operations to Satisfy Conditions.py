from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        dp = [[0] * 10 for _ in range(w)]
        for w_i in range(w):
            for target in range(10):
                tmp_cnt = 0
                for h_i in range(h):
                    if grid[h_i][w_i] != target:
                        tmp_cnt += 1
                dp[w_i][target] = tmp_cnt

                if w_i == 0:
                    continue
                min_cnt = min([cnt for i, cnt in enumerate(dp[w_i - 1]) if target != i])
                dp[w_i][target] += min_cnt
        return min(dp[-1])
