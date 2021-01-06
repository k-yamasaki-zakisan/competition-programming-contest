# https://leetcode.com/problems/combinations/
# Runtime: 72 ms, faster than 98.46% of Python3 online submissions for Combinations.
# Memory Usage: 15.6 MB, less than 66.48% of Python3 online submissions for Combinations.

class Solution:
    def combine(self, n: int, k: int) -> list:
        from itertools import combinations
        ans = []
        for v in combinations(range(1, n+1), k):
            ans.append(list(v))
        return ans
