# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
# Runtime: 42 ms, faster than 71.28% of Python3 online submissions for Binary String With Substrings Representing 1 To N.
# Memory Usage: 13.7 MB, less than 98.99% of Python3 online submissions for Binary String With Substrings Representing 1 To N.


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for num in range(1, n + 1):
            if bin(num)[2:] not in s:
                return False
        return True
