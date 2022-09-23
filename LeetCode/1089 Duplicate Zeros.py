# https://leetcode.com/problems/duplicate-zeros/
# Runtime: 70 ms, faster than 96.58% of Python3 online submissions for Duplicate Zeros.
# Memory Usage: 15 MB, less than 28.88% of Python3 online submissions for Duplicate Zeros.

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        len_arr = len(arr)
        step = [-1] * len_arr
        cnt = 0
        for i in range(len_arr):
            step[i] = cnt
            if arr[i] == 0:
                cnt += 1
        for i in range(len_arr - 1, -1, -1):
            if i + step[i] < len_arr:
                arr[i + step[i]] = arr[i]
                if arr[i + step[i]] == 0 and i + step[i] + 1 < len_arr:
                    arr[i + step[i] + 1] = 0
