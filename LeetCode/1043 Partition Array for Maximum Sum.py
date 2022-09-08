# https://leetcode.com/problems/partition-array-for-maximum-sum/
# Runtime: 1188 ms, faster than 37.86% of Python3 online submissions for Partition Array for Maximum Sum.
# Memory Usage: 14 MB, less than 70.32% of Python3 online submissions for Partition Array for Maximum Sum.


from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            end = i - 1
            start = max(i - 1 - k, -1)
            currMax = 0

            for p in range(end, start, -1):
                currMax = max(currMax, arr[p])
                dp[i] = max(dp[i], dp[p] + currMax * (i - p))

        return dp[-1]
