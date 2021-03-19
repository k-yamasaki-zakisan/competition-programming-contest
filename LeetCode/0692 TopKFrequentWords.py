# https://leetcode.com/problems/top-k-frequent-words/
# Runtime: 48 ms, faster than 95.38% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 14.5 MB, less than 39.36% of Python3 online submissions for Top K Frequent Words.

class Solution:
    def topKFrequent(self, words: list, k: int) -> list:
        from collections import Counter
        words_cnt = Counter(words)
        words_sort = sorted(words_cnt.items(), key=lambda x: x[0])
        words_sort = sorted(words_sort, key=lambda x: -x[1])
        ans = []
        for i in range(k):
            ans.append(words_sort[i][0])
        return ans
