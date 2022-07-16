from typing import List

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
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
        now_cnt = 1
        visited = [[False] * max_w for _ in range(max_h)]
        visited[start_h][start_w] = True

        def dfs(now_h: int, now_w: int, now_cnt: int):
            global ans
            if now_h == goal_h and now_w == goal_w:
                if now_cnt == wark_cnt:
                    return 1
                return 0

            for y, x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_h, next_w = now_h + y, now_w + x
                if (
                    0 <= next_h < max_h
                    and 0 <= next_w < max_w
                    and grid[next_h][next_w] != -1
                    and not visited[next_h][next_w]
                ):
                    now_cnt += 1
                    visited[next_h][next_w] = True
                    result = dfs(next_h, next_w, now_cnt)
                    now_cnt -= 1
                    visited[next_h][next_w] = False

        ans = dfs(start_h, start_w, now_cnt)
        return ans


grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
S = Solution()
print(S.uniquePathsIII(grid))
