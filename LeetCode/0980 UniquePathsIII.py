# https://leetcode.com/problems/unique-paths-iii/
# Runtime: 47 ms, faster than 98.76% of Python3 online submissions for Unique Paths III.
# Memory Usage: 14 MB, less than 55.75% of Python3 online submissions for Unique Paths III.

from typing import List


class Solution:
    def __init__(self):
        self.ans = 0
        self.now_cnt = 1

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        max_h = len(grid)
        max_w = len(grid[0])
        wark_cnt = 2
        for h in range(max_h):
            wark_cnt += grid[h].count(0)
            if 1 in grid[h]:
                start_h, start_w = h, grid[h].index(1)
            if 2 in grid[h]:
                goal_h, goal_w = h, grid[h].index(2)
        visited = [[False] * max_w for _ in range(max_h)]
        visited[start_h][start_w] = True

        def dfs(now_h: int, now_w: int):
            if now_h == goal_h and now_w == goal_w:
                if self.now_cnt == wark_cnt:
                    self.ans += 1
                return

            for y, x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_h, next_w = now_h + y, now_w + x
                if (
                    0 <= next_h < max_h
                    and 0 <= next_w < max_w
                    and grid[next_h][next_w] != -1
                    and not visited[next_h][next_w]
                ):
                    self.now_cnt += 1
                    visited[next_h][next_w] = True
                    dfs(next_h, next_w)
                    self.now_cnt -= 1
                    visited[next_h][next_w] = False

        dfs(start_h, start_w)
        return self.ans
