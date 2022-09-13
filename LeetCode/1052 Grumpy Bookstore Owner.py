# https://leetcode.com/problems/grumpy-bookstore-owner/
# Runtime: 729 ms, faster than 13.32% of Python3 online submissions for Grumpy Bookstore Owner.
# Memory Usage: 16.4 MB, less than 48.16% of Python3 online submissions for Grumpy Bookstore Owner.

from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        satisfied = not_satisfied = bonus = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                satisfied += customers[i]
            else:
                not_satisfied += customers[i]

            if minutes <= i and grumpy[i - minutes]:
                not_satisfied -= customers[i - minutes]
            bonus = max(bonus, not_satisfied)
        return satisfied + bonus
