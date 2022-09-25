from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque

        max_y, max_x = len(grid), len(grid[0])
        stack = deque()
        dp = [[-1] * max_x for _ in range(max_y)]
        if grid[0][0] == 0:
            stack.append((0, 0))
            dp[0][0] = 1
        while len(stack):
            now_y, now_x = stack.popleft()
            for next_y, next_x in [
                [now_y + 1, now_x],
                [now_y, now_x + 1],
                [now_y + 1, now_x + 1],
                [now_y + 1, now_x - 1],
                [now_y - 1, now_x + 1],
                [now_y - 1, now_x - 1],
                [now_y - 1, now_x],
                [now_y, now_x - 1],
            ]:
                if (
                    0 <= next_y < max_y
                    and 0 <= next_x < max_x
                    and grid[next_y][next_x] == 0
                    and dp[next_y][next_x] == -1
                ):
                    dp[next_y][next_x] = dp[now_y][now_x] + 1
                    stack.append((next_y, next_x))
        return dp[-1][-1]


S = Solution()
grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
print(S.shortestPathBinaryMatrix(grid))
