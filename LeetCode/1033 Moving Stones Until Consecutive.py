# https://leetcode.com/problems/moving-stones-until-consecutive/
# Runtime: 53 ms, faster than 32.73% of Python3 online submissions for Moving Stones Until Consecutive.
# Memory Usage: 13.9 MB, less than 29.09% of Python3 online submissions for Moving Stones Until Consecutive.

from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        if a + 2 == c:
            return [0, 0]
        elif min(c - b, b - a) < 3:
            return [1, c - a - 2]
        else:
            return [2, c - a - 2]
