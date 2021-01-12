# https://leetcode.com/problems/find-the-difference/
# Runtime: 32 ms, faster than 78.59% of Python3 online submissions for Find the Difference.
# Memory Usage: 14.3 MB, less than 57.84% of Python3 online submissions for Find the Difference.

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import defaultdict
        memo = defaultdict(int)
        for ss in s:
            memo[ss] += 1
        for tt in t:
            if tt not in memo or memo[tt] == 0:
                return tt
            else:
                memo[tt] -= 1
