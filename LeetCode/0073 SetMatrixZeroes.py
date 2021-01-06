# https://leetcode.com/problems/set-matrix-zeroes/
# Runtime: 172 ms, faster than 6.50% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 14.9 MB, less than 85.69% of Python3 online submissions for Set Matrix Zeroes.

class Solution:
    def setZeroes(self, matrix: list) -> None:
        def check_0(h: int, w: int):
            if matrix[h][w] == 0:
                self.set_0 = True
            else:
                if self.set_0:
                    matrix[h][w] = 'test'
        H, W = len(matrix), len(matrix[0])
        for h in range(H):
            self.set_0 = False
            for w in range(W):
                check_0(h, w)
            self.set_0 = False
            for w in range(W-1, -1, -1):
                check_0(h, w)
        for w in range(W):
            self.set_0 = False
            for h in range(H):
                check_0(h, w)
            self.set_0 = False
            for h in range(H-1, -1, -1):
                check_0(h, w)
        for h in range(H):
            for w in range(W):
                if matrix[h][w] == 'test':
                    matrix[h][w] = 0
        return matrix
