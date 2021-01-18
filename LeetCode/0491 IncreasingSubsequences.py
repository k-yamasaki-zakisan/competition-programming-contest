# https://leetcode.com/problems/increasing-subsequences/
# Runtime: 400 ms, faster than 21.57% of Python3 online submissions for Increasing Subsequences.
# Memory Usage: 22 MB, less than 53.83% of Python3 online submissions for Increasing Subsequences.

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        tmp = set()
        for i in range(2, len(nums)+1):
            for v in combinations(nums, i):
                tmp.add(v)
        ans = set()
        for t in tmp:
            ok_flag = True
            for i in range(1, len(t)):
                if t[i-1] > t[i]:
                    ok_flag = False
                    break
            if ok_flag:
                ans.add(t)
        return list(ans)
