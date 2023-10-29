from typing import List


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dp = [0] * n
        dp[0] = max(0, k - nums[0])
        dp[1] = max(0, k - nums[1])
        dp[2] = max(0, k - nums[2])

        for i in range(3, n):
            dp[i] = min(dp[i - 3 : i]) + max(0, k - nums[i])
        print(dp)
        return min(dp[n - 3 :])
