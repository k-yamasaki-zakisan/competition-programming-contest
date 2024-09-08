from typing import List


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        max_point = [[0, nums[0]]]

        for i in range(0, n):
            dp[-1] = max(nums[i] * (n - 1 - i) + dp[i], dp[-1])
            dp[i] = (i - max_point[-1][0]) * max_point[-1][1] + dp[max_point[-1][0]]
            if max_point[-1][-1] < nums[i]:
                max_point.append([i, nums[i]])
        return dp[-1]
