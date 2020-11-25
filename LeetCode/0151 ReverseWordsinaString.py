# https://leetcode.com/problems/reverse-words-in-a-string/
# Runtime: 32 ms, faster than 61.72% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 14.3 MB, less than 39.24% of Python3 online submissions for Reverse Words in a String.

class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split()
        words_list.reverse()
        return ' '.join(words_list)