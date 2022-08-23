# https://leetcode.com/problems/remove-outermost-parentheses/
# Runtime: 56 ms, faster than 59.93% of Python3 online submissions for Remove Outermost Parentheses.
# Memory Usage: 13.9 MB, less than 62.24% of Python3 online submissions for Remove Outermost Parentheses.


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        cnt = 0
        ans = ""
        for s in S:
            if s == "(":
                if 0 < cnt:
                    ans += s
                cnt += 1
            else:
                cnt -= 1
                if 0 < cnt:
                    ans += s
        return ans
