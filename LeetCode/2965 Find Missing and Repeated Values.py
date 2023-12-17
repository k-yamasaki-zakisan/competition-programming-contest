from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        memo = set()
        a, b = -1, -1
        for g in grid:
            for num in g:
                if num in memo:
                    a = num
                memo.add(num)
        n = len(grid)
        for num in range(1, n**2 + 1):
            if num not in memo:
                b = num
        return [a, b]
