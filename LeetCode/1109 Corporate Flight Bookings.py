# https://leetcode.com/problems/corporate-flight-bookings/
# Runtime: 1201 ms, faster than 71.64% of Python3 online submissions for Corporate Flight Bookings.
# Memory Usage: 28 MB, less than 69.17% of Python3 online submissions for Corporate Flight Bookings.

from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n + 2)
        for s, g, cnt in bookings:
            ans[s] += cnt
            ans[g + 1] -= cnt
        for i in range(1, len(ans)):
            ans[i] += ans[i - 1]
        return ans[1:-1]
