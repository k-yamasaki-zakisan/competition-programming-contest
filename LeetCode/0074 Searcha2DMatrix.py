# https://leetcode.com/problems/search-a-2d-matrix/
# Runtime: 44 ms, faster than 58.67% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.7 MB, less than 53.57% of Python3 online submissions for Search a 2D Matrix.

class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        from bisect import bisect_left
        H, W = len(matrix), len(matrix[0])
        for h in range(H):
            if matrix[h][0] <= target <= matrix[h][-1]:
                i = bisect_left(matrix[h], target)
                if matrix[h][i] == target:
                    return True
            elif target <= matrix[h][0]:
                break
        return False
