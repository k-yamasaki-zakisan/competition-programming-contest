# https://leetcode.com/problems/length-of-last-word/
# Runtime: 32 ms, faster than 48.27% of Python3 online submissions for Length of Last Word.
# Memory Usage: 14.4 MB, less than 29.27% of Python3 online submissions for Length of Last Word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s_list = s.split(' ')
        return len(s_list[-1])
