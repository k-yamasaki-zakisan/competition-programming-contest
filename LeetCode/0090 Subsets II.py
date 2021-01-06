# https://leetcode.com/problems/subsets-ii/
# Runtime: 40 ms, faster than 48.80% of Python3 online submissions for Subsets II.
# Memory Usage: 14.4 MB, less than 46.84% of Python3 online submissions for Subsets II.

class Solution:
    def subsetsWithDup(self, nums: list) -> list:
        from itertools import combinations
        nums.sort()
        if len(nums) == 0:
            return []
        ans = [[]]
        for i in range(1, len(nums)+1):
            for v in set(combinations(nums, i)):
                ans.append(list(v))
        return ans
