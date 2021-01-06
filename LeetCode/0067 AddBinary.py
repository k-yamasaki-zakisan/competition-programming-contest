# https://leetcode.com/problems/add-binary/
# Runtime: 32 ms, faster than 73.77% of Python3 online submissions for Add Binary.
# Memory Usage: 14.3 MB, less than 47.88% of Python3 online submissions for Add Binary.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        ans = ''
        add = 0
        for i in range(max_len-1, -1, -1):
            tmp = int(a[i])+int(b[i])+add
            add = 0
            if 1 < tmp:
                tmp = tmp % 2
                add = 1
            ans = str(tmp)+ans
        if add:
            ans = str(add)+ans
        return ans
