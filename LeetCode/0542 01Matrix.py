# https://leetcode.com/problems/01-matrix/
# Runtime: 676 ms, faster than 66.11% of Python3 online submissions for 01 Matrix.
# Memory Usage: 17.4 MB, less than 34.09% of Python3 online submissions for 01 Matrix.

class Solution:
    def updateMatrix(self, matrix: list) -> list:
        from collections import deque
        H = len(matrix)
        W = len(matrix[0])
        stack = deque([])
        dp = [[-1]*W for _ in range(H)]
        for h in range(H):
            for w in range(W):
                if matrix[h][w] == 0:
                    stack.append([h, w])
                    dp[h][w] = 0
        while len(stack):
            h, w = stack.popleft()
            for y, x in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nh, nw = h+y, w+x
                if 0 <= nh < H and 0 <= nw < W:
                    if dp[nh][nw] == -1:
                        dp[nh][nw] = dp[h][w]+1
                        stack.append([nh, nw])
        return dp
