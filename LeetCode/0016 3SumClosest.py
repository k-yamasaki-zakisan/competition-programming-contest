# https://leetcode.com/problems/3sum-closest/

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