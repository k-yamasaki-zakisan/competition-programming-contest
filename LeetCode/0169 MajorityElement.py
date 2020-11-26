# https://leetcode.com/problems/majority-element/
# Runtime: 164 ms, faster than 53.58% of Python3 online submissions for Majority Element.
# Memory Usage: 15.7 MB, less than 5.72% of Python3 online submissions for Majority Element.

class Solution:
    def majorityElement(self, nums: list) -> int:
        memo = {}
        for num in nums:
            if num in memo:
                memo[num] += 1
            else:
                memo[num] = 1
        print(memo)
        for key,val in memo.items():
            if len(nums)//2 < val:
                return key
        return -1