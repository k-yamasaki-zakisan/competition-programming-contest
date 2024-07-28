from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        single_digit_nums_sum = sum([num for num in nums if num < 10])
        return nums_sum - single_digit_nums_sum != single_digit_nums_sum
