# https://leetcode.com/problems/max-area-of-island/
# Runtime: 136 ms, faster than 78.72% of Python3 online submissions for Max Area of Island.
# Memory Usage: 14.5 MB, less than 86.22% of Python3 online submissions for Max Area of Island.

from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        W: int = len(grid[0])
        H: int = len(grid)
        ans = 0
        checked = [[0]*W for _ in range(H)]

        for h in range(H):
            for w in range(W):
                if checked[h][w]:
                    continue
                checked[h][w] = 1
                if grid[h][w]:
                    tmp_cnt = 1
                    stack = deque([[h, w]])
                    while len(stack):
                        h, w = stack.popleft()
                        for y, x in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                            nh, nw = h+y, w+x
                            if 0 <= nh < H and 0 <= nw < W:
                                if grid[nh][nw] and checked[nh][nw] == 0:
                                    checked[nh][nw] = 1
                                    stack.append([nh, nw])
                                    tmp_cnt += 1
                    ans = max(ans, tmp_cnt)
        return ans
