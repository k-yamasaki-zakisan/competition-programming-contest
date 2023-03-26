# https://leetcode.com/contest/weekly-contest-338/problems/minimum-operations-to-make-all-array-elements-equal/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        from bisect import bisect

        nums.sort()
        n = len(nums)
        max_num, min_num = nums[-1], nums[0]
        sum_num = sum(nums)
        ans = []
        ruiseki = [nums[0]]
        for i in range(1, n):
            ruiseki.append(ruiseki[-1] + nums[i])
        for query in queries:
            if min_num < query < max_num:
                i = bisect(nums, query)
                tmp_f = query * i - ruiseki[i - 1]
                tmp_s = (ruiseki[-1] - ruiseki[i - 1]) - query * (n - i)
                ans.append(tmp_f + tmp_s)
            else:
                ans.append(abs(query * n - sum_num))
        return ans
