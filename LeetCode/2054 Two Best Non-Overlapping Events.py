from typing import List
from heapq import heappop, heappush


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        max_value = 0
        ans = 0

        for start, end, value in events:
            while pq and pq[0][0] < start:
                max_value = max(max_value, heappop(pq)[1])

            ans = max(ans, max_value + value)
            heappush(pq, (end, value))

        return ans
