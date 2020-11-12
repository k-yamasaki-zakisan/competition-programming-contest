# https://leetcode.com/problems/single-number/
# Runtime: 136 ms, faster than 29.18% of Python3 online submissions for Single Number.
# Memory Usage: 16.8 MB, less than 50.17% of Python3 online submissions for Single Number.

class Solution:
    def singleNumber(self, nums: list) -> int:
        nums_cnt = {}
        for i,val in enumerate(nums):
            if val in nums_cnt:
                nums_cnt[val] += 1
            else:
                nums_cnt[val] = 1
        for key,val in nums_cnt.items():
            if val%2:
                return key