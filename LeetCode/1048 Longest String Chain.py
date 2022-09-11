# https://leetcode.com/problems/longest-string-chain/
# Runtime: 402 ms, faster than 32.29% of Python3 online submissions for Longest String Chain.
# Memory Usage: 14.2 MB, less than 88.80% of Python3 online submissions for Longest String Chain.

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        max_chain_length = 1
        map_word_to_count = {}
        for word in sorted(words, key=len):
            map_word_to_count[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1 :]
                if predecessor in map_word_to_count:
                    map_word_to_count[word] = max(
                        map_word_to_count[predecessor] + 1, map_word_to_count[word]
                    )
                    max_chain_length = max(max_chain_length, map_word_to_count[word])
        return max_chain_length
