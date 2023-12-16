from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        H, W = len(grid), len(grid[0])
        h_cnt = [sum(g) for g in grid]
        w_cnt = [0] * W
        for w in range(W):
            tmp = 0
            for h in range(H):
                tmp += grid[h][w]
            w_cnt[w] = tmp
        ans = [[0] * W for _ in range(H)]
        for h in range(H):
            for w in range(W):
                ans[h][w] = h_cnt[h] + w_cnt[w] - (H - h_cnt[h]) - (W - w_cnt[w])
        return ans
