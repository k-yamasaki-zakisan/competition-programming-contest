# https://leetcode.com/problems/keyboard-row/
# Runtime: 32 ms, faster than 55.06% of Python3 online submissions for Keyboard Row.
# Memory Usage: 14 MB, less than 94.08% of Python3 online submissions for Keyboard Row.

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for word in words:
            s_word = word.lower()
            if len([1 for w in s_word if w in 'qwertyuiop']) == len(word) or len([1 for w in s_word if w in 'asdfghjkl']) == len(word) or len([1 for w in s_word if w in 'zxcvbnm']) == len(word):
                ans.append(word)
        return ans
