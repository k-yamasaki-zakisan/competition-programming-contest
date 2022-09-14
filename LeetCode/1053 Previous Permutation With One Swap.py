# https://leetcode.com/problems/previous-permutation-with-one-swap/
# Runtime: 496 ms, faster than 20.40% of Python3 online submissions for Previous Permutation With One Swap.
# Memory Usage: 15.3 MB, less than 84.13% of Python3 online submissions for Previous Permutation With One Swap.

from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        len_arr, i_s = len(arr), -1
        for i in range(len_arr - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                i_s = i - 1
                break
        if i_s == -1:
            return arr

        t_num, i_t = -1, -1
        for i in range(i_s + 1, len_arr):
            if t_num < arr[i] < arr[i_s]:
                t_num, i_t = arr[i], i
        arr[i_t], arr[i_s] = arr[i_s], arr[i_t]
        return arr
