# https://leetcode.com/problems/contiguous-array/
# Runtime: 844 ms, faster than 79.84% of Python3 online submissions for Contiguous Array.
# Memory Usage: 22.6 MB, less than 6.42% of Python3 online submissions for Contiguous Array.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        summ, res = 0, {0: [-1]}
        for pos, num in enumerate(nums):
            summ += 1 if num else -1
            res.setdefault(summ, []).append(pos)
        return max(val[-1] - val[0] for val in res.values())
