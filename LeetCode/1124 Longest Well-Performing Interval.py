# https://leetcode.com/problems/longest-well-performing-interval/
# Runtime: 577 ms, faster than 17.02% of Python3 online submissions for Longest Well-Performing Interval.
# Memory Usage: 14.5 MB, less than 78.84% of Python3 online submissions for Longest Well-Performing Interval.

from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ans, tmp = 0, 0
        memo = {}
        for i in range(len(hours)):
            tmp += 1 if 8 < hours[i] else -1
            if 0 < tmp:
                ans = i + 1
            else:
                if tmp not in memo:
                    memo[tmp] = i
                if tmp - 1 in memo:
                    ans = max(ans, i - memo[tmp - 1])
        return ans
