# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# Runtime: 1241 ms, faster than 86.20% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
# Memory Usage: 15.2 MB, less than 22.74% of Python3 online submissions for Minimum Domino Rotations For Equal Row.

from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for num in set([tops[0], bottoms[0]]):
            if all(num in d for d in zip(tops, bottoms)):
                return len(tops) - max(tops.count(num), bottoms.count(num))
        return -1
