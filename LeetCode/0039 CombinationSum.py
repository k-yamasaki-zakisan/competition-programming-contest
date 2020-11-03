# https://leetcode.com/problems/combination-sum/
# Runtime: 164 ms, faster than 14.60% of Python3 online submissions for Combination Sum.
# Memory Usage: 14.3 MB, less than 7.11% of Python3 online submissions for Combination Sum.

class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        ans = []
        self.dfs(candidates, target, [], ans)
        return ans
    
    def dfs(self, nums:list, target:int, path, ans:list) -> list:
        if target < 0:
            return 
        if target == 0:
            ans.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ans)