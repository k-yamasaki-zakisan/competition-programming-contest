# https://leetcode.com/problems/most-common-word/
# Runtime: 36 ms, faster than 65.36% of Python3 online submissions for Most Common Word.
# Memory Usage: 14.3 MB, less than 75.02% of Python3 online submissions for Most Common Word.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict
        words = defaultdict(int)
        paragraph = paragraph.lower()
        for c in "!?.;',":
            paragraph = paragraph.replace(c, ' ')
        paragraph_list = paragraph.split(' ')
        for word in paragraph_list:
            if len(word) == 0:
                continue
            word = word.lower()
            words[word] += 1
        for ban in banned:
            if ban.lower() in words:
                del words[ban]
        count, word = max((count, word) for word, count in words.items())
        return word
