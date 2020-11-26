# https://leetcode.com/problems/excel-sheet-column-number/
# Runtime: 32 ms, faster than 59.97% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 14.4 MB, less than 8.52% of Python3 online submissions for Excel Sheet Column Number.

class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        len_n = len(s)-1
        i = 0
        while 0 < len_n:
            alf = s[i]
            n = ord(alf)-64
            ans += n*26**len_n
            len_n -= 1
            i += 1
        ans += ord(s[-1])-64

        return ans