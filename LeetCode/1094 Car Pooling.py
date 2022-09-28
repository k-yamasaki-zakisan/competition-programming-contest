# https://leetcode.com/problems/car-pooling/
# Runtime: 154 ms, faster than 35.23% of Python3 online submissions for Car Pooling.
# Memory Usage: 14.4 MB, less than 41.46% of Python3 online submissions for Car Pooling.

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cs = [0] * (1000 + 1)
        for p, f, t in trips:
            cs[f] += p
            cs[t] -= p
        for i in range(1, len(cs)):
            cs[i] += cs[i - 1]
        return len([i for i in cs if capacity < i]) == 0
