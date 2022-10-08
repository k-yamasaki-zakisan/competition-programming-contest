# https://leetcode.com/problems/relative-sort-array/
# Runtime: 74 ms, faster than 41.86% of Python3 online submissions for Relative Sort Array.
# Memory Usage: 14 MB, less than 77.43% of Python3 online submissions for Relative Sort Array.

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter

        arr1_count = Counter(arr1)
        ans = []
        for a in arr2:
            ans += [a] * arr1_count[a]
            del arr1_count[a]
        arr1_count = sorted(arr1_count.items(), key=lambda x: x[0])
        for key, val in arr1_count:
            ans += [key] * val
        return ans
