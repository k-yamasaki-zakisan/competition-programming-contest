# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
# Runtime: 42 ms, faster than 99.39% of Python3 online submissions for Maximize Sum Of Array After K Negations.
# Memory Usage: 14 MB, less than 59.42% of Python3 online submissions for Maximize Sum Of Array After K Negations.

from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        abs_num = min([abs(num) for num in nums])
        ans = sum(nums)
        for i in range(min(k, len(nums))):
            if nums[i] < 0:
                ans += 2 * abs(nums[i])
            else:
                cnt = k - i
                if cnt % 2:
                    ans -= abs_num * 2
                return ans
        if len(nums) < k:
            ans -= abs_num * 2
        return ans
