# https://leetcode.com/problems/di-string-match/
# Runtime: 129 ms, faster than 7.68% of Python3 online submissions for DI String Match.
# Memory Usage: 15.2 MB, less than 45.00% of Python3 online submissions for DI String Match.

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]
