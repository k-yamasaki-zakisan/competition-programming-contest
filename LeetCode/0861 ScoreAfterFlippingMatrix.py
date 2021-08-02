# https://leetcode.com/problems/score-after-flipping-matrix/
# Runtime: 44 ms, faster than 24.14% of Python3 online submissions for Score After Flipping Matrix.
# Memory Usage: 14.3 MB, less than 66.46% of Python3 online submissions for Score After Flipping Matrix.

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        from copy import deepcopy
        def check(grid:List[List[int]]) -> int:
            H = len(grid)
            W = len(grid[0])
            for w in range(1, W):
                tmp_cnt = 0
                for h in range(H):
                    if grid[h][w]:
                        tmp_cnt += 1
                if tmp_cnt <= H//2:
                    for h in range(H):
                        if grid[h][w]:
                            grid[h][w] = 0
                        else:
                            grid[h][w] = 1
            result = 0
            for h in range(H):
                tmp = grid[h]
                tmp = ''.join(map(str, tmp))
                result += int(tmp, base=2)
            return result

        H = len(grid)
        W = len(grid[0])
        head_cnt = 0
        for h in range(H):
            if grid[h][0]:
                head_cnt += 1
        if head_cnt == 0:
            for h in range(H):
                grid[h][0] = 1
            return check(grid)
        elif head_cnt == H:
            return check(grid)
        else:
            grid_1 = deepcopy(grid)
            grid_2 = deepcopy(grid)
            for h in range(H):
                if grid_1[h][0]:
                    for w in range(1,W):
                        grid_1[h][w] = 0 if grid_1[h][w] else 1
                else:
                    grid_1[h][0] = 1
            for h in range(H):
                if not grid_2[h][0]:
                    for w in range(W):
                        grid_2[h][w] = 0 if grid_2[h][w] else 1
            return max(check(grid_1), check(grid_2))