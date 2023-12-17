from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        from bisect import bisect_left

        n = len(nums)
        nums.sort()
        mid = nums[n // 2]
        palindromic_list = []
        degit = len(str(mid)) // 2
        for num in range(10 ** (max(degit, 1))):
            if num < 10:
                palindromic_list.append(num)
            left_str = str(num)
            right_str = left_str[::-1]
            palindromic_list.append(int(left_str + right_str))
            for i in range(10):
                palindromic_list.append(int(left_str + str(i) + right_str))
        palindromic_list.sort()
        target_i = bisect_left(palindromic_list, mid)
        return min(
            sum([abs(palindromic_list[target_i] - num) for num in nums]),
            sum([abs(palindromic_list[target_i - 1] - num) for num in nums]),
        )
