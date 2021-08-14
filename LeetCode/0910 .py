# https://leetcode.com/problems/smallest-range-ii/
# Runtime: 202 ms, faster than 8.12% of Python3 online submissions for Smallest Range II.
# Memory Usage: 15.3 MB, less than 82.66% of Python3 online submissions for Smallest Range II.


class Solution:
    def smallestRangeII(self, nums: List[int], K: int) -> int:
        nums.sort()
        mi, ma = nums[0], nums[-1]
        ans = ma-mi
        for i in range(len(nums)-1):
            a, b = nums[i], nums[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans
