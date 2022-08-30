# https://leetcode.com/problems/longest-arithmetic-subsequence/
# Runtime: 81 ms, faster than 19.81% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 13.8 MB, less than 78.84% of Python3 online submissions for Two City Scheduling.

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = [(b - a) for a, b in costs]
        diff.sort()
        return sum(diff[: len(costs) // 2]) + sum([a for a, b in costs])

        # ans = 0
        # diff = []
        # for a,b in costs:
        #     ans += a
        #     diff.append(b-a)
        # diff.sort()
        # for i in range(len(diff)//2):
        #     ans += diff[i]
        # return ans
