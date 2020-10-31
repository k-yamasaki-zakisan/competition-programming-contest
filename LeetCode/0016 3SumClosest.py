# https://leetcode.com/problems/3sum-closest/
# Runtime: 352 ms, faster than 15.81% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 14.2 MB, less than 99.98% of Python3 online submissions for 3Sum Closest.

class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        sa = 10**10
        ans = 0
        for i in range(len(nums)-2):
            left = i+1
            right  = len(nums)-1
            while left < right:
                sums = nums[i]+nums[left]+nums[right]
                if abs(sums-target) < sa:
                    sa = abs(sums-target)
                    ans = sums
                if sums-target < 0:
                    left += 1
                elif 0 <= sums-target:
                    right -= 1
        return ans