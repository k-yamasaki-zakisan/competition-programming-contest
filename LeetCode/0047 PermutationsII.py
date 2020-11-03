# https://leetcode.com/problems/permutations-ii/
# Runtime: 64 ms, faster than 42.20% of Python3 online submissions for Permutations II.
# Memory Usage: 14.4 MB, less than 5.01% of Python3 online submissions for Permutations II.

class Solution:
    def permuteUnique(self, nums: list) -> list:
        from collections import Counter
        result = []
        def backtrack(comb:list, counter:dict):
            if len(comb) == len(nums):
                result.append(list(comb))
                return
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb,counter)
                    comb.pop()
                    counter[num] += 1
        backtrack([], Counter(nums))
        return result