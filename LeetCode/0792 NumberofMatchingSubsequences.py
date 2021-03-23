# https://leetcode.com/problems/number-of-matching-subsequences/
# Runtime: 636 ms, faster than 47.02% of Python3 online submissions for Number of Matching Subsequences.
# Memory Usage: 17.3 MB, less than 30.52% of Python3 online submissions for Number of Matching Subsequences.


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        from collections import defaultdict
        from bisect import bisect_right
        memo = defaultdict(list)
        for i, ss in enumerate(s):
            memo[ss].append(i)
        ans = 0
        for word in words:
            ok_flag = True
            index = -1
            for s in word:
                s_index = bisect_right(memo[s], index)
                if len(memo[s]) == s_index or len(memo[s]) == 0:
                    ok_flag = False
                    break
                index = memo[s][s_index]
            if ok_flag:
                ans += 1
        return ans
