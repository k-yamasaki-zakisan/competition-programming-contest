# https://leetcode.com/problems/maximum-product-of-three-numbers/submissions/
# Runtime: 252 ms, faster than 72.55 % of Python3 online submissions for Maximum Product of Three Numbers.
# Memory Usage: 15.7 MB, less than 7.23 % of Python3 online submissions for Maximum Product of Three Numbers.

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])
