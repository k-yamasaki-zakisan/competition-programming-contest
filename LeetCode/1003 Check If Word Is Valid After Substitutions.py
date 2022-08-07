# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
# Runtime: 80 ms, faster than 63.36% of Python3 online submissions for Check If Word Is Valid After Substitutions.
# Memory Usage: 14.1 MB, less than 51.94% of Python3 online submissions for Check If Word Is Valid After Substitutions.


class Solution:
    def isValid(self, S: str) -> bool:
        words = []
        for s in S:
            if 2 <= len(words) and words[-2] == "a" and words[-1] == "b" and s == "c":
                words.pop()
                words.pop()
            else:
                words.append(s)
        return True if len(words) == 0 else False
