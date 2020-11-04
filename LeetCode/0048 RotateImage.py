# https://leetcode.com/problems/rotate-image/
# Runtime: 32 ms, faster than 82.67% of Python3 online submissions for Rotate Image.
# Memory Usage: 14.3 MB, less than 99.99% of Python3 online submissions for Rotate Image.

class Solution:
    def rotate(self, matrix: list) -> None:
        N = len(matrix)
        for i in range(N):
            for j in range(i,N):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for i in range(N):
            matrix[i].reverse()

