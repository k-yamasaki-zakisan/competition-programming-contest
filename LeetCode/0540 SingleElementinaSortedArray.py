# https://leetcode.com/problems/single-element-in-a-sorted-array/
# Runtime: 76 ms, faster than 22.39% of Python3 online submissions for Single Element in a Sorted Array.
# Memory Usage: 16.3 MB, less than 75.21% of Python3 online submissions for Single Element in a Sorted Array.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        from collections import defaultdict
        memo = defaultdict(int)
        for num in nums:
            memo[num] += 1
        for key, val in memo.items():
            if val == 1:
                return key
