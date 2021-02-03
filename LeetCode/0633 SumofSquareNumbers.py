# https://leetcode.com/problems/sum-of-square-numbers/
# Runtime: 336 ms, faster than 35.03% of Python3 online submissions for Sum of Square Numbers.
# Memory Usage: 14.4 MB, less than 26.98% of Python3 online submissions for Sum of Square Numbers.

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c**0.5)+1):
            c_sa = c-i**2
            if c_sa == int(c_sa**0.5)**2:
                return True
        return False
