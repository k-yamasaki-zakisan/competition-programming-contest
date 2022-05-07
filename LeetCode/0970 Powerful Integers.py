# https://leetcode.com/problems/powerful-integers/
# Runtime: 53 ms, faster than 31.31% of Python3 online submissions for Powerful Integers.
# Memory Usage: 13.7 MB, less than 97.98% of Python3 online submissions for Powerful Integers.

from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        from bisect import bisect_right

        x_pow, y_pow = [1], [1]
        ans = set()
        while x_pow[-1] <= bound and x != 1:
            x_pow.append(x_pow[-1] * x)
        while y_pow[-1] <= bound and y != 1:
            y_pow.append(y_pow[-1] * y)
        for x_base in x_pow:
            if bound <= x_base:
                break
            tar = bound - x_base
            i_b = bisect_right(y_pow, tar)
            for i in range(i_b):
                ans.add(x_base + y_pow[i])
        return sorted(list(ans))
