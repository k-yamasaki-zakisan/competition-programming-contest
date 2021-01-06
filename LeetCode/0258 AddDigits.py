# https://leetcode.com/problems/add-digits/
# Runtime: 32 ms, faster than 65.79% of Python3 online submissions for Add Digits.
# Memory Usage: 14.3 MB, less than 37.16% of Python3 online submissions for Add Digits.

class Solution:
    def addDigits(self, num: int) -> int:
        while 9 < num:
            str_num = str(num)
            tmp = 0
            for s in str_num:
                tmp += int(s)
            num = tmp
        return num
