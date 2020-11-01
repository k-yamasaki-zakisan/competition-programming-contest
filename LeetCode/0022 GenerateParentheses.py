# https://leetcode.com/problems/generate-parentheses/
# Runtime: 36 ms, faster than 55.28% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.4 MB, less than 8.94% of Python3 online submissions for Generate Parentheses.

class Solution:
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans