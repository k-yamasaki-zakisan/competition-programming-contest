# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list) -> int:
        ans = 0
        r = len(height)-1
        l = 0
        while l < r:
            h = min(height[r],height[l])
            ans = max(ans, h*(r-l))
            if height[r] == h:
                r -= 1
            else:
                l += 1
        return ans