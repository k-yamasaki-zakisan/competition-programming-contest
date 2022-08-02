# https://leetcode.com/problems/number-of-squareful-arrays/
# Runtime: 44 ms, faster than 71.62% of Python3 online submissions for Number of Squareful Arrays.
# Memory Usage: 13.8 MB, less than 86.04% of Python3 online submissions for Number of Squareful Arrays.

from typing import List


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        self.ans = set()

        def dfs(tmp_nums, nums):
            if len(nums) == 0:
                self.ans.add("".join([str(num) for num in tmp_nums]))
                return

            for i in range(len(nums)):
                if 0 < i and nums[i] == nums[i - 1]:
                    continue
                if len(tmp_nums) == 0 or (
                    0 < len(tmp_nums)
                    and int((nums[i] + tmp_nums[-1]) ** 0.5) ** 2
                    == nums[i] + tmp_nums[-1]
                ):
                    dfs(tmp_nums + [nums[i]], nums[:i] + nums[i + 1 :])

        dfs([], nums)
        return len(self.ans)
