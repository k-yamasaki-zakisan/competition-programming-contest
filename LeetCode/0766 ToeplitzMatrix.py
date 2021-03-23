# https://leetcode.com/problems/toeplitz-matrix/
# Runtime: 84 ms, faster than 79.28% of Python3 online submissions for Toeplitz Matrix.
# Memory Usage: 14.5 MB, less than 8.21% of Python3 online submissions for Toeplitz Matrix.


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        H = len(matrix)
        W = len(matrix[0])
        for h in range(H-1, -1, -1):
            target = matrix[h][0]
            w = 0
            result = self.check(matrix, w, h, W, H, target)
            if result == False:
                return False

        for w in range(W):
            target = matrix[0][w]
            h = 0
            result = self.check(matrix, w, h, W, H, target)
            if result == False:
                return False

        return True

    def check(self, matrix: List[List[int]], w: int, h: int, W: int, H: int, target: int) -> bool:
        while 0 <= h < H and 0 <= w < W and matrix[h][w] == target:
            h += 1
            w += 1
        if 0 <= h < H and 0 <= w < W and matrix[h][w] != target:
            return False

        return True
