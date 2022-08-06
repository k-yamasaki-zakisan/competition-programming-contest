# https://leetcode.com/problems/find-common-characters/
# Runtime: 47 ms, faster than 96.83% of Python3 online submissions for Find Common Characters.
# Memory Usage: 13.9 MB, less than 65.26% of Python3 online submissions for Find Common Characters.

from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter

        grand_cnt = Counter(words[0])
        for i in range(len(words)):
            word = words[i]
            word_cnt = Counter(word)
            tmp = {}
            for key, val in word_cnt.items():
                if key in grand_cnt:
                    tmp[key] = min(grand_cnt[key], word_cnt[key])
            grand_cnt = tmp

        grand_cnt = sorted(grand_cnt.items(), key=lambda x: x[0])
        ans = []
        for key, val in grand_cnt:
            ans += [key] * val
        return ans
