# https://leetcode.com/problems/single-number-iii/
# Runtime: 56 ms, faster than 84.54% of Python3 online submissions for Single Number III.
# Memory Usage: 16.2 MB, less than 17.81% of Python3 online submissions for Single Number III.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        kind_cnt = defaultdict(int)
        for num in nums:
            kind_cnt[num] += 1
        ans = []
        for key, val in kind_cnt.items():
            if val == 1:
                ans.append(key)
        return ans
