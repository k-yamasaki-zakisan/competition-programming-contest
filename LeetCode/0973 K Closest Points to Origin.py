# https://leetcode.com/problems/k-closest-points-to-origin/
# Runtime: 833 ms, faster than 86.06% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 20.4 MB, less than 60.76% of Python3 online submissions for K Closest Points to Origin.

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = [[x**2 + y**2, x, y] for x, y in points]
        ans = sorted(ans, key=lambda x: x[0])
        return [[x, y] for p, x, y in ans[:k]]
