# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Runtime: 34 ms, faster than 92.88% of Python3 online submissions for Greatest Common Divisor of Strings.
# Memory Usage: 13.8 MB, less than 75.54% of Python3 online submissions for Greatest Common Divisor of Strings.


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd

        if str1 + str2 != str2 + str1:
            return ""
        i = gcd(len(str1), len(str2))
        return str1[:i]
