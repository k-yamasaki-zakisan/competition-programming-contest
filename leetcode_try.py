from typing import List

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


def isAlienSorted(words: List[str], order: str) -> bool:
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


words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))
