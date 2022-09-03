# https://leetcode.com/problems/valid-boomerang/
# Runtime: 57 ms, faster than 34.41% of Python3 online submissions for Valid Boomerang.
# Memory Usage: 13.9 MB, less than 62.70% of Python3 online submissions for Valid Boomerang.

from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if (points[1][1] - points[0][1]) * (points[2][0] - points[0][0]) == (
            points[2][1] - points[0][1]
        ) * (points[1][0] - points[0][0]):
            return False
        return True
