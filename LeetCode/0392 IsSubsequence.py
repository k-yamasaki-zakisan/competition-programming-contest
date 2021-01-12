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


# Runtime: 36 ms, faster than 32.10% of Python3 online submissions for Is Subsequence.
# Memory Usage: 14.4 MB, less than 23.25% of Python3 online submissions for Is Subsequence.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        s_index = 0
        for t_index in range(len(t)):
            if t[t_index] == s[s_index]:
                s_index += 1
            if s_index >= len(s):
                return True
        return False
