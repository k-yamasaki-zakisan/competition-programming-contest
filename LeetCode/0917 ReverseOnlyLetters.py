# https://leetcode.com/problems/reverse-only-letters/
# Runtime: 24 ms, faster than 95.59% of Python3 online submissions for Reverse Only Letters.
# Memory Usage: 14.2 MB, less than 47.70% of Python3 online submissions for Reverse Only Letters.

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)
