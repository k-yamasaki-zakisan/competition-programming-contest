# https://leetcode.com/problems/degree-of-an-array/
# Runtime: 216 ms, faster than 93.98% of Python3 online submissions for Degree of an Array.
# Memory Usage: 15.5 MB, less than 74.44% of Python3 online submissions for Degree of an Array.


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import Counter
        nums_cnt = Counter(nums)
        max_cnt = max(nums_cnt.values())

        ans = 10**10
        left = {}
        right = {}
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i

        for num, cnt in nums_cnt.items():
            if max_cnt != cnt:
                continue
            ans = min(ans, right[num]-left[num]+1)
        return ans
