from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        from collections import deque
        from heapq import heappop, heappush

        thif_diff = deque()
        H, W = len(grid), len(grid[0])
        diff_memo = [[-1] * W for _ in range(H)]
        for h in range(H):
            for w in range(W):
                if grid[h][w] == 1:
                    thif_diff.append([h, w, 0])
                    diff_memo[h][w] = 0
        while len(thif_diff):
            now_h, now_w, diff = thif_diff.popleft()
            for next_h, next_w in [
                [now_h + 1, now_w],
                [now_h - 1, now_w],
                [now_h, now_w + 1],
                [now_h, now_w - 1],
            ]:
                if (
                    0 <= next_h < H
                    and 0 <= next_w < W
                    and diff_memo[next_h][next_w] == -1
                ):
                    next_diff = diff + 1
                    diff_memo[next_h][next_w] = next_diff
                    thif_diff.append([next_h, next_w, next_diff])
        first_move = [[-diff_memo[0][0], 0, 0]]
        sec_move = []
        visited = [[-1] * W for _ in range(H)]
        visited[0][0] = diff_memo[0][0]
        while True:
            while len(first_move):
                diff, now_h, now_w = heappop(first_move)
                diff = -diff
                for next_h, next_w in [
                    [now_h + 1, now_w],
                    [now_h - 1, now_w],
                    [now_h, now_w + 1],
                    [now_h, now_w - 1],
                ]:
                    if (
                        0 <= next_h < H
                        and 0 <= next_w < W
                        and visited[next_h][next_w] == -1
                    ):
                        if diff <= diff_memo[next_h][next_w]:
                            visited[next_h][next_w] = diff
                            heappush(first_move, [-diff, next_h, next_w])
                        else:
                            heappush(
                                sec_move,
                                [
                                    -diff_memo[next_h][next_w],
                                    next_h,
                                    next_w,
                                    now_h,
                                    now_w,
                                ],
                            )
            while len(sec_move):
                diff, now_h, now_w, ex_h, ex_w = heappop(sec_move)
                diff = -diff
                if visited[now_h][now_w] == -1:
                    visited[now_h][now_w] = diff
                    heappush(first_move, [-diff, now_h, now_w])
            if visited[-1][-1] != -1:
                return visited[-1][-1]
