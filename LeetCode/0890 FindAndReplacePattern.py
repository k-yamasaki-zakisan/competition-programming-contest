# https://leetcode.com/problems/find-and-replace-pattern/
# Runtime: 24 ms, faster than 97.93% of Python3 online submissions for Find and Replace Pattern.
# Memory Usage: 14.2 MB, less than 84.09% of Python3 online submissions for Find and Replace Pattern.

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        from collections import defaultdict
        pattern_memo = defaultdict(list)
        for i, p in enumerate(pattern):
            pattern_memo[p].append(i)
        pattern_memo_list = list(pattern_memo.values())
        ans = []
        for word in words:
            tmp = defaultdict(list)
            for i, w in enumerate(word):
                tmp[w].append(i)
            if list(tmp.values()) == pattern_memo_list:
                ans.append(word)
        return ans
