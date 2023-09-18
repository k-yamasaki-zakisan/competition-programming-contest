from typing import List


class Solution:
    def __init__(self):
        self.ans = 10**10

    def minimumMoves(self, grid: List[List[int]]) -> int:
        def dps(zeros, extras, dps_grid, count):
            if len(zeros) == 0:
                self.ans = min(self.ans, count)
                return
            for i in range(len(zeros)):
                zh, zw = zeros[i]
                for j in range(len(extras)):
                    eh, ew, extra = extras[j]
                    next_count = count + abs(zh - eh) + abs(zw - ew)
                    next_extras = []
                    for k in range(len(extras)):
                        if k == j:
                            extra -= 1
                            if extra == 0:
                                continue
                            next_extras.append([eh, ew, extra])
                        else:
                            next_extras.append(extras[k])
                    dps(zeros[:i] + zeros[i + 1 :], next_extras, dps_grid, next_count)

        H, W = len(grid), len(grid[0])
        zero_points = []
        extra_points = []
        for h in range(H):
            for w in range(W):
                if grid[h][w] == 0:
                    zero_points.append([h, w])
                if 1 < grid[h][w]:
                    extra_points.append([h, w, grid[h][w] - 1])

        if len(zero_points) == 0:
            return 0

        dps(zero_points, extra_points, grid, 0)
        return self.ans
