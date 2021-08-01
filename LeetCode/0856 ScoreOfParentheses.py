# https://leetcode.com/problems/score-of-parentheses/
# Runtime: 28 ms, faster than 82.88% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 14.3 MB, less than 43.26% of Python3 online submissions for Score of Parentheses.

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        from copy import copy
        s = list(s)
        loop_flag = True
        while loop_flag:
            loop_flag = False
            tmp = []
            for i,ss in enumerate(s):
                if len(tmp) and tmp[-1].isdigit() and ss.isdigit():
                    tmp[-1] = str(int(tmp[-1])+int(ss))
                elif ss == ')':
                    if tmp[-1] == '(':
                        s = tmp[:-1]+['1']+s[i+1:]
                    else:
                        s = tmp[:-2]+[str(int(tmp[-1])*2)]+s[i+1:]
                    loop_flag = True
                    break
                else:
                    tmp.append(ss)
        return int(tmp[-1])