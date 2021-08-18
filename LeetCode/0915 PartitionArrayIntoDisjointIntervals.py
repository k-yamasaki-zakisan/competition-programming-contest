# https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# Runtime: 1260 ms, faster than 5.02% of Python3 online submissions for Partition Array into Disjoint Intervals.
# Memory Usage: 28.3 MB, less than 5.03% of Python3 online submissions for Partition Array into Disjoint Intervals.

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        l_memo, r_memo = [0]*N, [0]*N
        l_memo[0], r_memo[-1] = nums[0], nums[-1]
        for i in range(1, N):
            l_memo[i] = max(l_memo[i-1], nums[i])
        for i in range(N-2, -1, -1):
            r_memo[i] = min(r_memo[i+1], nums[i])
        for i in range(N-1):
            if l_memo[i] <= r_memo[i+1]:
                return i+1
