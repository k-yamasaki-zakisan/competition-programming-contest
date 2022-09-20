# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
# Runtime: 1512 ms, faster than 43.40% of Python3 online submissions for Number of Submatrices That Sum to Target.
# Memory Usage: 14.9 MB, less than 72.44% of Python3 online submissions for Number of Submatrices That Sum to Target.

from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        from collections import defaultdict

        m, n = len(matrix), len(matrix[0])
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y + 1] += matrix[x][y]
        res = 0
        for y1 in range(n):
            for y2 in range(y1, n):
                preSums = defaultdict(int)
                preSums[0] += 1
                s = 0
                for x in range(m):
                    s += matrix[x][y2] - (matrix[x][y1 - 1] if y1 > 0 else 0)
                    res += preSums[s - target]
                    preSums[s] += 1
        return res
