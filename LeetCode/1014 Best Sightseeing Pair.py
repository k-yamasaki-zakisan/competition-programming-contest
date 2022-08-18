# https://leetcode.com/problems/best-sightseeing-pair/
# Runtime: 527 ms, faster than 86.84% of Python3 online submissions for Best Sightseeing Pair.
# Memory Usage: 20.4 MB, less than 85.64% of Python3 online submissions for Best Sightseeing Pair.

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_num = values[0]
        ans = 0
        for i in range(1, len(values)):
            ans = max(ans, max_num + values[i] - i)
            max_num = max(max_num, values[i] + i)
        return ans
