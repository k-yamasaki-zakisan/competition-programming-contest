# https://leetcode.com/problems/camelcase-matching/
# Runtime: 51 ms, faster than 52.15% of Python3 online submissions for Camelcase Matching.
# Memory Usage: 13.8 MB, less than 99.67% of Python3 online submissions for Camelcase Matching.

from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        len_pat = len(pattern)
        for query in queries:
            i = 0
            flag = True
            for q in query:
                if i < len_pat and q == pattern[i]:
                    i += 1
                elif q.isupper():
                    flag = False
                    break
            if flag and i == len_pat:
                ans.append(True)
            else:
                ans.append(False)

        return ans
