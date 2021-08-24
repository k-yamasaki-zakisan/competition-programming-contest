# https://leetcode.com/problems/minimum-falling-path-sum/
# Runtime: 152 ms, faster than 25.43% of Python3 online submissions for Minimum Falling Path Sum.
# Memory Usage: 15.2 MB, less than 39.39% of Python3 online submissions for Minimum Falling Path Sum.

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        H, W = len(matrix), len(matrix[0])
        dp = [[float('inf')]*W for _ in range(H)]
        for w in range(W):
            dp[0][w] = matrix[0][w]
        for h in range(H-1):
            for w in range(W):
                for x in [-1, 0, 1]:
                    nw = w+x
                    if not 0 <= nw < W:
                        continue
                    dp[h+1][nw] = min(dp[h+1][nw], dp[h][w]+matrix[h+1][nw])
        return min(dp[-1])
