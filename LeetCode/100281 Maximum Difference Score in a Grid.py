from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        INF = 10**8
        cands = []
        H, W = len(grid), len(grid[0])
        for h in range(H):
            for w in range(W):
                cands.append([grid[h][w], h, w])
        cands.sort()
        ans = -INF
        visited = [[False] * W for _ in range(H)]
        while len(cands):
            now_v, now_h, now_w = cands.pop()
            if visited[now_h][now_w]:
                continue
            for next_h in range(now_h, -1, -1):
                for next_w in range(now_w, -1, -1):
                    if next_h == now_h and next_w == now_w:
                        continue
                    if visited[next_h][next_w]:
                        break
                    visited[next_h][next_w] = True
                    if (
                        grid[next_h][next_w] <= grid[next_h][now_w]
                        or grid[next_h][next_w] <= grid[now_h][next_w]
                    ):
                        ans = max(ans, grid[now_h][now_w] - grid[next_h][next_w])
        return ans
