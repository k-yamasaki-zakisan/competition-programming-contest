# https://leetcode.com/problems/word-subsets/
# Runtime: 992 ms, faster than 42.45% of Python3 online submissions for Word Subsets.
# Memory Usage: 18 MB, less than 89.71% of Python3 online submissions for Word Subsets.

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d = Counter()
        for word in B:
            cnt = Counter(word)
            for key in set(list(d) + list(cnt)):
                d[key] = max(d[key], cnt[key])
        return [x for x in A if all([d[key] <= x.count(key) for key in d.keys()])]
