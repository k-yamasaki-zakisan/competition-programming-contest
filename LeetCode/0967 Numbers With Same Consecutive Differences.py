# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
# Runtime: 48 ms, faster than 69.19% of Python3 online submissions for Numbers With Same Consecutive Differences.
# Memory Usage: 14.1 MB, less than 77.03% of Python3 online submissions for Numbers With Same Consecutive Differences.

from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        nums = [str(i) for i in range(1, 10)]
        for _ in range(n - 1):
            tmp = []
            for num in nums:
                last = int(num[-1])
                if 0 <= last - k <= 9:
                    tmp.append(num + str(last - k))
                if k == 0:
                    continue
                if 0 <= last + k <= 9:
                    tmp.append(num + str(last + k))
            nums = tmp
        return nums
