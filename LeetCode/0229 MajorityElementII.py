# https://leetcode.com/problems/majority-element-ii/
# Runtime: 116 ms, faster than 59.19% of Python3 online submissions for Majority Element II.
# Memory Usage: 15.4 MB, less than 18.63% of Python3 online submissions for Majority Element II.

class Solution:
    def majorityElement(self, nums: list) -> list:
        from collections import defaultdict
        memo = defaultdict(int)
        len_nums = len(nums)
        for num in nums:
            memo[num] += 1
        ans = []
        for key, val in memo.items():
            if len_nums < val*3:
                ans.append(key)
        return ans
