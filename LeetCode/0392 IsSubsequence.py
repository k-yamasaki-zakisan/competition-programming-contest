# https://leetcode.com/problems/is-subsequence/
# Runtime: 60 ms, faster than 7.91% of Python3 online submissions for Is Subsequence.
# Memory Usage: 14.2 MB, less than 72.13% of Python3 online submissions for Is Subsequence.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ss in s:
            is_exit = False
            while i < len(t):
                if t[i] == ss:
                    i += 1
                    is_exit = True
                    break
                i += 1
            if is_exit == False:
                return False
        return True
