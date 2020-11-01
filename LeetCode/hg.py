# https://leetcode.com/problems/valid-parentheses/
# Runtime: 24 ms, faster than 94.39% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        start = ['(', '{', '[']
        end = {')':'(', '}':'{', ']':'['}
        for sa in s:
            if sa in start:
                ans.append(sa)
            elif sa in end:
                if len(ans):
                    if ans[-1] == end[sa]:
                        ans.pop()
                    else:
                        return False
                else:
                    return False
        if len(ans):
            return False
        else:
            return True