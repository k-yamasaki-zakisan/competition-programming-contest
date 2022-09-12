# https://leetcode.com/problems/height-checker/
# Runtime: 76 ms, faster than 15.00% of Python3 online submissions for Height Checker.
# Memory Usage: 13.9 MB, less than 56.03% of Python3 online submissions for Height Checker.

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_heights = sorted(heights)
        diff = 0
        for i in range(len(heights)):
            if heights[i] != sort_heights[i]:
                diff += 1
        return diff
