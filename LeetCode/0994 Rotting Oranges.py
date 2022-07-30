# https://leetcode.com/problems/rotting-oranges/
# Runtime: 61 ms, faster than 82.77% of Python3 online submissions for Rotting Oranges.
# Memory Usage: 13.9 MB, less than 91.59% of Python3 online submissions for Rotting Oranges.

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        H = len(grid)
        W = len(grid[0])
        start = deque()
        visited = [[-1] * W for _ in range(H)]
        mikan_cnt = 0
        for h in range(H):
            for w in range(W):
                if grid[h][w] == 2:
                    start.append((h, w))
                    visited[h][w] = 0
                if grid[h][w] == 1:
                    mikan_cnt += 1
        if mikan_cnt == 0:
            return 0
        que = deque(start)
        while len(que):
            nowh, noww = que.popleft()
            for y, x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nexth, nextw = nowh + y, noww + x
                if (
                    0 <= nexth < H
                    and 0 <= nextw < W
                    and visited[nexth][nextw] == -1
                    and grid[nexth][nextw] == 1
                ):
                    visited[nexth][nextw] = visited[nowh][noww] + 1
                    que.append((nexth, nextw))
        ans = -1
        for h in range(H):
            for w in range(W):
                if grid[h][w] == 1 and visited[h][w] == -1:
                    return -1
                ans = max(ans, visited[h][w])
        return ans
