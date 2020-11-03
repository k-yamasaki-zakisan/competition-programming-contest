# https://leetcode.com/problems/combination-sum-ii/
# Runtime: 92 ms, faster than 54.92% of Python3 online submissions for Combination Sum II.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Combination Sum II.

class Solution:
    def combinationSum2(self:list, candidates:list, target:int) -> list:
        ret = []
        self.dfs(sorted(candidates), target, 0, [], ret)
        return ret
    
    def dfs(self, nums:list, target:int, idx:int, path:list, ret:list):
        if target <= 0:
            if target == 0:
                ret.append(path)
            return 
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ret)