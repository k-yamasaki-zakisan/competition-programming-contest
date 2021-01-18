# https://leetcode.com/problems/partition-equal-subset-sum/
# Runtime: 1308 ms, faster than 49.74% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 14.9 MB, less than 57.58% of Python3 online submissions for Partition Equal Subset Sum.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target_nums = sum(nums)/2
        P = set([nums[0]])
        for num in nums[1:]:
            for p in list(P):
                P.add(num+p)
        return target_nums in P
