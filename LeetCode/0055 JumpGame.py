# https://leetcode.com/problems/jump-game/
# Runtime: 84 ms, faster than 75.67% of Python3 online submissions for Jump Game.
# Memory Usage: 16.2 MB, less than 99.99% of Python3 online submissions for Jump Game.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0
        for i in range(len(nums)):
            if max_i < i:
                return False
            max_i = max(max_i,i+nums[i])
        return True