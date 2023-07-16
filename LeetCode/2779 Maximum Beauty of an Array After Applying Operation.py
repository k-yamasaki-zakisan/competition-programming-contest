from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        memo = [0] * (max_num + k + 10)
        for num in nums:
            memo[max(0, num - k)] += 1
            memo[num + k + 1] -= 1
        for i in range(1, len(memo)):
            memo[i] += memo[i - 1]
        return max(memo)
