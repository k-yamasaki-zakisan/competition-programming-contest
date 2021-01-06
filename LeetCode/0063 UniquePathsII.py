# https://leetcode.com/problems/unique-paths-ii/
# Runtime: 40 ms, faster than 78.36% of Python3 online submissions for Unique Paths II.
# Memory Usage: 14.2 MB, less than 69.99% of Python3 online submissions for Unique Paths II.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        H, W = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*W for _ in range(H)]
        for h in range(H):
            for w in range(W):
                if h == 0 and w == 0:
                    dp[h][w] = 1
                elif (h == 0 or w == 0) and obstacleGrid[h][w] == 0:
                    if (h == 0 and dp[h][w-1] == 0) \
                            or (w == 0 and dp[h-1][w] == 0):
                        continue
                    dp[h][w] = 1
                elif obstacleGrid[h][w] == 0:
                    dp[h][w] = dp[h-1][w]+dp[h][w-1]
        return dp[-1][-1]
