from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        exact_nums = sorted(nums)
        N = len(nums)
        tmp = nums
        if nums == exact_nums:
            return 0
        for i in range(N):
            last_num = tmp.pop()
            tmp = [last_num] + tmp
            if exact_nums == tmp:
                return i + 1
        return -1
