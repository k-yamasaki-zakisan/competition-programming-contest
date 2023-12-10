from typing import List


class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        from collections import defaultdict

        MOD = 10**9 + 7
        n = len(nums)
        memo = defaultdict(list)
        for i, num in enumerate(nums):
            memo[num].append(i)
        partitions = []
        for i in range(n):
            num = nums[i]
            if len(partitions) == 0:
                partitions.append([memo[num][0], memo[num][-1]])
                continue
            if partitions[-1][-1] < memo[num][0]:
                partitions.append([memo[num][0], memo[num][-1]])
                continue
            partitions[-1][-1] = max(memo[num][-1], partitions[-1][-1])
        return pow(2, len(partitions) - 1, MOD)
