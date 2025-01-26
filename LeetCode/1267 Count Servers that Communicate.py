from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        H, W = len(grid), len(grid[0])
        visited = [[False] * W for _ in range(H)]
        for h in range(H):
            tmp = 0
            for w in range(W):
                if grid[h][w] == 1:
                    tmp += 1
            if 1 < tmp:
                for w in range(W):
                    if grid[h][w] == 1 and not visited[h][w]:
                        visited[h][w] = True
                        ans += 1
        for w in range(W):
            tmp = 0
            for h in range(H):
                if grid[h][w] == 1:
                    tmp += 1
            if 1 < tmp:
                for h in range(H):
                    if grid[h][w] == 1 and not visited[h][w]:
                        visited[h][w] = True
                        ans += 1
        return ans
