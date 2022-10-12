# https://leetcode.com/problems/number-of-equivalent-domino-pairs/
# Runtime: 527 ms, faster than 37.71% of Python3 online submissions for Number of Equivalent Domino Pairs.
# Memory Usage: 23.8 MB, less than 67.96% of Python3 online submissions for Number of Equivalent Domino Pairs.

from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        from collections import defaultdict

        memo = defaultdict(int)
        ans = 0
        for a, b in dominoes:
            if b < a:
                a, b = b, a
            ans += memo[(a, b)]
            memo[(a, b)] += 1
        return ans
