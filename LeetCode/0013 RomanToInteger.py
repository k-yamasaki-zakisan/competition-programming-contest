# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        trans = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000
        }
        len_s = len(s)
        i = ans = 0
        while i < len_s:
            if i+1 < len_s and s[i:i+2] in trans:
                ans += trans[s[i:i+2]]
                i += 2
            else:
                ans += trans[s[i]]
                i += 1
        return ans