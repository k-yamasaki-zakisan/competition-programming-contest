# https://leetcode.com/problems/combination-sum-iii/
# Runtime: 40 ms, faster than 8.37% of Python3 online submissions for Combination Sum III.
# Memory Usage: 14.4 MB, less than 9.15% of Python3 online submissions for Combination Sum III.

class Solution:
    def combinationSum3(self, k: int, n: int) -> list:
        import copy
        nums = [i for i in range(1,10)]
        ans = []
        tmp_list = []
        def dps(start) -> int:
            for i in range(start, 9):
                tmp_list.append(nums[i])
                if len(tmp_list) == k:
                    if sum(tmp_list) == n:
                        ans.append(copy.copy(tmp_list))
                else:
                    if i < 9:
                        dps(i+1)
                tmp_list.pop()
        dps(0)
        return ans


# Runtime: 32 ms, faster than 61.96% of Python3 online submissions for Combination Sum III.
# Memory Usage: 14.4 MB, less than 9.15% of Python3 online submissions for Combination Sum III.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        from itertools import combinations
        nums = [i for i in range(1,10)]
        ans = []
        for v in combinations(nums, k):
            if sum(v) == n:
                ans.append(list(v))
        return ans