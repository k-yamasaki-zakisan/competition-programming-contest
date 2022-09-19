# https://leetcode.com/problems/adding-two-negabinary-numbers/
# Runtime: 152 ms, faster than 12.80% of Python3 online submissions for Adding Two Negabinary Numbers.
# Memory Usage: 14.1 MB, less than 16.95% of Python3 online submissions for Adding Two Negabinary Numbers.


from typing import List

enumerate


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        len_arr1, len_arr2 = len(arr1), len(arr2)
        target = 0
        for i in range(len_arr1):
            if arr1[i]:
                target += pow(-2, len_arr1 - i - 1)
        for i in range(len_arr2):
            if arr2[i]:
                target += pow(-2, len_arr2 - i - 1)

        if target == 0:
            return [0]
        ans = []
        while target != 0:
            if target % 2 != 0:
                target -= 1
                ans = [1] + ans
            else:
                ans = [0] + ans
            target //= -2
        return ans
