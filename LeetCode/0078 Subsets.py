# https://leetcode.com/problems/subsets/
# Runtime: 36 ms, faster than 48.79% of Python3 online submissions for Subsets.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Subsets.

class Solution:
    def subsets(self, nums: list) -> list:
        n = len(nums)
        ans = []
        for i in range(2 ** n):
            bag = []
            for j in range(n):
                if ((i >> j) & 1):
                    bag.append(nums[j])
            ans.append(bag)
        return ans