# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/description/
# Beats 37.21%
# Memory 13.8 MB

from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)

        odd_big_cnt = 0
        for i in range(1, n, 2):
            min_num = nums[i - 1]
            if i + 1 < n:
                min_num = min(min_num, nums[i + 1])
            odd_big_cnt += max(0, nums[i] - min_num + 1)

        even_big_cnt = 0
        for i in range(0, n, 2):
            min_num = 2000
            if 0 <= i - 1:
                min_num = min(min_num, nums[i - 1])
            if i + 1 < n:
                min_num = min(min_num, nums[i + 1])
            even_big_cnt += max(0, nums[i] - min_num + 1)

        return min(odd_big_cnt, even_big_cnt)
