# https://leetcode.com/problems/convert-to-base-2/
# Runtime: 45 ms, faster than 63.86% of Python3 online submissions for Convert to Base -2.
# Memory Usage: 13.9 MB, less than 55.45% of Python3 online submissions for Convert to Base -2.


class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = ""
        while n != 0:
            if n % 2 != 0:
                n -= 1
                ans = "1" + ans
            else:
                ans = "0" + ans
            n //= -2
        return ans
