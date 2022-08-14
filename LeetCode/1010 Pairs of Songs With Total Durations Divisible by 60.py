# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# Runtime: 435 ms, faster than 55.17% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
# Memory Usage: 18.3 MB, less than 35.70% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.

from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        from collections import defaultdict

        ans = 0
        single = defaultdict(int)
        for t in time:
            t %= 60
            ans += single[(60 - t % 60) % 60]
            single[t] += 1
        return ans
