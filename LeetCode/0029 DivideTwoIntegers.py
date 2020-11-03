# https://leetcode.com/problems/divide-two-integers/
# Runtime: 32 ms, faster than 68.01% of Python3 online submissions for Divide Two Integers.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Divide Two Integers.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (0 <= dividend and 0 <= divisor) or (dividend < 0 and divisor < 0):
            ans = dividend//divisor
        else:
            if dividend%divisor:
                ans = dividend//divisor+1
            else:
                ans = dividend//divisor
        print(ans)
        if -2147483648 < ans < 2147483648:
            return ans
        elif 2147483648 <= ans:
            return 2147483647
        elif ans <= -2147483648:
            return -2147483648