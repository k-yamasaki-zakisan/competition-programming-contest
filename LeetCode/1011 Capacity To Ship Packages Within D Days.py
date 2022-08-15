# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# Runtime: 820 ms, faster than 44.82% of Python3 online submissions for Capacity To Ship Packages Within D Days.
# Memory Usage: 17 MB, less than 96.85% of Python3 online submissions for Capacity To Ship Packages Within D Days.

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = min(weights), sum(weights) + 100
        while 1 < r - l:
            mid = (l + r) // 2
            cnt = 1
            tmp_w = 0
            for w in weights:
                if tmp_w + w < mid:
                    tmp_w += w
                else:
                    cnt += 1
                    tmp_w = w
            if cnt <= days:
                r = mid
            else:
                l = mid
        return max(l, max(weights))
