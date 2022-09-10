# https://leetcode.com/problems/last-stone-weight/
# Runtime: 34 ms, faster than 90.62% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.9 MB, less than 62.65% of Python3 online submissions for Last Stone Weight.

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heapify, heappop, heappush

        stones_nu = [-num for num in stones]
        heapify(stones_nu)
        while 1 < len(stones_nu):
            f = heappop(stones_nu)
            s = heappop(stones_nu)
            if f != s:
                heappush(stones_nu, -abs(f - s))
        return -stones_nu[0] if len(stones_nu) else 0
