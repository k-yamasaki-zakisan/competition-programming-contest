# https://leetcode.com/problems/verifying-an-alien-dictionary/
# Runtime: 34 ms, faster than 93.34% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 13.9 MB, less than 85.33% of Python3 online submissions for Verifying an Alien Dictionary.


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ex_trans_words = ""
        trans = {o: chr(ord("a") + i) for i, o in enumerate(order)}
        for i, word in enumerate(words):
            tmp_word = ""
            for w in word:
                tmp_word += trans[w]
            if i and ex_trans_words > tmp_word:
                return False
            ex_trans_words = tmp_word
        return True
