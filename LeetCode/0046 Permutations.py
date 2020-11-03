# https://leetcode.com/problems/permutations/
# Runtime: 36 ms, faster than 86.21% of Python3 online submissions for Permutations.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools
        ans = []
        for v in itertools.permutations(nums):
            ans.append(v)
        return ans


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def f(num, perm):
            newP = []
            for p in perm:
                for i in range(len(p) + 1):
                    newP.append(p[:i] + [num] + p[i:])
            return newP
        
        if len(nums) <= 1:
            return [nums]
        perm = [[]]
        for num in nums:
            perm = f(num, perm)
        return perm