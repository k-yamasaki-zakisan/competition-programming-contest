from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        from collections import deque

        H, W = len(grid), len(grid[0])
        visited = [[False] * W for _ in range(H)]
        ans = 0
        for h in range(H):
            for w in range(W):
                if not (grid[h][w] == 1 and not visited[h][w]):
                    continue
                flag = True if (w not in [0, W - 1] and h not in [0, H - 1]) else False
                cnt = 1
                visited[h][w] = True
                stack = deque([[h, w]])
                while len(stack):
                    now_h, now_w = stack.popleft()
                    for y, x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        next_h, next_w = now_h + y, now_w + x
                        if (
                            0 <= next_h < H
                            and 0 <= next_w < W
                            and grid[next_h][next_w] == 1
                            and not visited[next_h][next_w]
                        ):
                            visited[next_h][next_w] = True
                            cnt += 1
                            stack.append([next_h, next_w])
                            if next_w in [0, W - 1] or next_h in [0, H - 1]:
                                flag = False
                if flag:
                    ans += cnt

        return ans


n = [
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
]

S = Solution()
print(S.numEnclaves(n))
