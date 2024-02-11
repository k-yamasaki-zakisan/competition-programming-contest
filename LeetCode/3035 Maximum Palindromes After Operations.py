from typing import List


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        from collections import defaultdict

        odd_words, even_words = [], []
        memo = defaultdict(int)
        for word in words:
            if len(word) % 2:
                odd_words.append(len(word))
            else:
                even_words.append(len(word))
            for w in word:
                memo[w] += 1
        odd_cnt, even_cnt = 0, 0
        for val in memo.values():
            odd_cnt += val % 2
            even_cnt += (val // 2) * 2
        odd_words.sort(reverse=True)
        ans = 0
        while odd_cnt and len(odd_words):
            odd_word = odd_words.pop()
            odd_cnt -= 1
            if 0 == odd_word - 1:
                ans += 1
            else:
                even_words.append(odd_word - 1)
        even_words.sort(reverse=True)
        while len(even_words) and even_cnt:
            even_word = even_words.pop()
            if even_word <= even_cnt:
                even_cnt -= even_word
                ans += 1
        while len(odd_words) and even_cnt:
            odd_word = odd_words.pop()
            if odd_word <= even_cnt:
                even_cnt -= odd_word
                ans += 1
        return ans
