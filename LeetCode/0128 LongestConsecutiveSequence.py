# https://leetcode.com/problems/longest-consecutive-sequence/
# Runtime: 56 ms, faster than 58.74% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 15.2 MB, less than 5.11% of Python3 online submissions for Longest Consecutive Sequence.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums)) 
        nums.sort()
        ans = 1
        pre_v = nums[0]
        tmp_ans = 1
        for i in range(1,len(nums)):
            if pre_v+1 == nums[i]:
                tmp_ans += 1
            else:
                tmp_ans = 1
            pre_v = nums[i]
            ans = max(ans,tmp_ans)
        return ans