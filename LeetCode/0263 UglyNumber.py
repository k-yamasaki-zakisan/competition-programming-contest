# https://leetcode.com/problems/ugly-number/
# Runtime: 36 ms, faster than 28.03% of Python3 online submissions for Ugly Number.
# Memory Usage: 14.4 MB, less than 8.80% of Python3 online submissions for Ugly Number.

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False

        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5

        if num == 1:
            ans = True
        else:
            ans = False
        return ans
