# https://leetcode.com/problems/excel-sheet-column-title/
# Runtime: 28 ms, faster than 66.63% of Python3 online submissions for Excel Sheet Column Title.
# Memory Usage: 14.1 MB, less than 72.50% of Python3 online submissions for Excel Sheet Column Title.

class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n > 0:
            r = n%26
            if r == 0: r = 26
            s = chr(64+r)+s
            n = (n-r)//26
        return s