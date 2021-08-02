# https://leetcode.com/problems/transpose-matrix/
# Runtime: 68 ms, faster than 88.41% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 14.9 MB, less than 65.15% of Python3 online submissions for Transpose Matrix.

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        H = len(matrix)
        W = len(matrix[0])
        ans = [[0]*H for _ in range(W)]
        for h in range(H):
            for w in range(W):
                ans[w][h] = matrix[h][w]
        return ans