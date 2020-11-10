# https://leetcode.com/problems/minimum-path-sum/
# Runtime: 160 ms, faster than 8.39% of Python3 online submissions for Minimum Path Sum.
# Memory Usage: 15.5 MB, less than 6.49% of Python3 online submissions for Minimum Path Sum.

class Solution:
    def minPathSum(self, grid: list) -> int:
        from collections import deque 
        H = len(grid)
        W = len(grid[0])
        dp = [[10**10]*W for _ in range(H)]
        dp[0][0] = grid[0][0]
        stack = deque([[0,0]])
        while stack:
            h,w = stack.popleft()
            for y,x in [[1,0],[0,1]]:
                if 0 <= h+y <= H-1 and 0 <= w+x <= W-1:
                    dp[h+y][w+x] = min(dp[h+y][w+x], dp[h][w]+grid[h+y][w+x])
                    if len(stack) == 0:
                        stack.append([h+y,w+x])
                    else:
                        if stack[-1] != [h+y,w+x]:
                            stack.append([h+y,w+x])
        return dp[-1][-1]


# Runtime: 96 ms, faster than 72.34% of Python3 online submissions for Minimum Path Sum.
# Memory Usage: 15.3 MB, less than 6.49% of Python3 online submissions for Minimum Path Sum.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) < 1:
            return 0
        m, n = len(grid), len(grid[0])
        min_path = [[0] * n for _ in range(m)]
        min_path[0][0] = grid[0][0]
        for c in range(1, n):
            min_path[0][c] = min_path[0][c-1] + grid[0][c]
        for r in range(1, m):
            min_path[r][0] = min_path[r-1][0] + grid[r][0]
        for r in range(1, m):
            for c in range(1, n):
                min_path[r][c] = min(min_path[r-1][c], min_path[r][c-1]) + grid[r][c]
        return min_path[m-1][n-1]