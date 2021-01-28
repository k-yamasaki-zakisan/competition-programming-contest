# https://leetcode.com/problems/k-diff-pairs-in-an-array/
# Runtime: 68 ms, faster than 94.94% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.7 MB, less than 47.34% of Python3 online submissions for K-diff Pairs in an Array.

class Solution:
    def findPairs(self, nums: list, k: int) -> int:
        from collections import Counter
        nums_cnt = Counter(nums)
        if k == 0:
            return len([key for key, val in nums_cnt.items() if 1 < val])

        ans = 0
        for key, val in nums_cnt.items():
            if key+k in nums_cnt:
                ans += 1
        return ans
