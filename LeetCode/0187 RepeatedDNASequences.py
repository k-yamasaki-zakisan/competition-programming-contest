# https://leetcode.com/problems/repeated-dna-sequences/
# Runtime: 48 ms, faster than 98.01% of Python3 online submissions for Repeated DNA Sequences.
# Memory Usage: 26.4 MB, less than 58.01% of Python3 online submissions for Repeated DNA Sequences.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list:
        cnd = set()
        ans = set()
        for i in range(len(s)-9):
            tmp = s[i:i+10]
            if tmp in cnd:
                ans.add(tmp)
            else:
                cnd.add(tmp)
        return ans
