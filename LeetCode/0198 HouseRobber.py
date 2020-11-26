# https://leetcode.com/problems/house-robber/
# Runtime: 24 ms, faster than 94.35% of Python3 online submissions for House Robber.
# Memory Usage: 14.2 MB, less than 36.74% of Python3 online submissions for House Robber.

class Solution:
    def rotate(self, nums: list, k: int) -> None:
        if not nums:
            return 0 
        
        if len(nums) <= 2:
            return max(nums)
        
        rob = [0]*len(nums)
        rob[0] = nums[0]
        rob[1] = nums[1]
            
        for i in range(1, len(nums)):
            rob[i] = max(rob[i-1], nums[i] + rob[i-2])
            
        return rob[-1]