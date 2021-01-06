# https://leetcode.com/problems/plus-one/
# Runtime: 28 ms, faster than 87.28% of Python3 online submissions for Plus One.
# Memory Usage: 14.3 MB, less than 11.33% of Python3 online submissions for Plus One.

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


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         i = len(digits) - 1
#         while i >= 0 :
#             if digits[i] + 1 > 9:
#                 digits[i] = 0
#                 i -= 1
#             else:
#                 digits[i] += 1
#                 return digits
#         digits.insert(0,1)
#         return digits
