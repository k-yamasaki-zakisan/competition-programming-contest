# https://leetcode.com/problems/first-unique-character-in-a-string/
# Runtime: 100 ms, faster than 72.20% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.8 MB, less than 6.26% of Python3 online submissions for First Unique Character in a String.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import defaultdict
        memo = defaultdict(int)
        for ss in s:
            memo[ss] += 1
        if 1 in memo.values():
            key = [k for k, v in memo.items() if v == 1][0]
            return list(s).index(key)
        else:
            return -1
