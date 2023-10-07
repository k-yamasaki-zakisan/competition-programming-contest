from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter

        count_nums = Counter(nums)
        ans = 0
        for val in count_nums.values():
            if val == 1:
                return -1
            three_times = val // 3
            if (val - three_times * 3) % 2 != 0:
                three_times -= 1
            ans += three_times
            val -= three_times * 3
            ans += val // 2
        return ans
