# https://leetcode.com/problems/word-pattern/
# Runtime: 24 ms, faster than 93.92% of Python3 online submissions for Word Pattern.
# Memory Usage: 14.4 MB, less than 21.55% of Python3 online submissions for Word Pattern.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        from collections import defaultdict
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        pattern_posi = defaultdict(list)
        for i, p in enumerate(pattern):
            pattern_posi[p].append(i)
        for p_lists in pattern_posi.values():
            if 1 < len(set([s[p_list] for p_list in p_lists])):
                return False
        s_posi = defaultdict(list)
        for i, ss in enumerate(s):
            s_posi[ss].append(i)
        for s_lists in s_posi.values():
            if 1 < len(set([pattern[s_list] for s_list in s_lists])):
                return False
        return True
