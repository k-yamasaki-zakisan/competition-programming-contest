# https://leetcode.com/problems/clumsy-factorial/
# Runtime: 64 ms, faster than 65.29% of Python3 online submissions for Clumsy Factorial.
# Memory Usage: 13.8 MB, less than 82.38% of Python3 online submissions for Clumsy Factorial.


class Solution:
    def clumsy(self, n: int) -> int:
        minus = 0
        plus = 0
        minus_num = 1
        for i in range(n):
            num = n - i
            if i % 4 == 0 or i % 4 == 1:
                minus_num *= num
            elif i % 4 == 2:
                minus_num //= num
                if i // 4 == 0:
                    minus += minus_num
                else:
                    minus -= minus_num
                minus_num = 1
            else:
                plus += num
        if n % 4 == 1 or n % 4 == 2:
            if i // 4 == 0:
                minus += minus_num
            else:
                minus -= minus_num
        ans = minus + plus
        return ans
