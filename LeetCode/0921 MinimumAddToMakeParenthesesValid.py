# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Runtime: 32 ms, faster than 59.89% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
# Memory Usage: 14.2 MB, less than 42.84% of Python3 online submissions for Minimum Add to Make Parentheses Valid.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        r = ans = 0
        for ss in s:
            if ss == '(':
                r += 1
            else:
                if r == 0:
                    ans += 1
                else:
                    r -= 1
        return ans+r
