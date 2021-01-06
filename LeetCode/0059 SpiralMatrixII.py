# https://leetcode.com/problems/spiral-matrix-ii/
# Runtime: 32 ms, faster than 74.44% of Python3 online submissions for Spiral Matrix II.
# Memory Usage: 14.1 MB, less than 97.33% of Python3 online submissions for Spiral Matrix II.

class Solution:
    def generateMatrix(self, n: int) -> list:
        ans = [[0]*n for _ in range(n)]
        ans[0][0] = 1
        move = [0, 1]
        cnt = 1
        h = w = 0
        while cnt != n*n:
            cnt += 1
            if (0 <= h+move[0] < n and 0 <= w+move[1] < n) == False \
                    or ans[h+move[0]][w+move[1]] != 0:
                if move == [0, 1]:
                    move = [1, 0]
                elif move == [1, 0]:
                    move = [0, -1]
                elif move == [0, -1]:
                    move = [-1, 0]
                elif move == [-1, 0]:
                    move = [0, 1]
            h += move[0]
            w += move[1]
            ans[h][w] = cnt
        return ans
