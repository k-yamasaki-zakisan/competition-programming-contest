# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Runtime: 96 ms, faster than 90.29% of Python3 online submissions for Largest Rectangle in Histogram.
# Memory Usage: 16 MB, less than 9.13% of Python3 online submissions for Largest Rectangle in Histogram.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        heights.append(0)
        
        res = 0
        for right in range(1,len(heights)):
            while stack and heights[stack[-1]] > heights[right]:
                h = heights[stack.pop()]
                left = -1 if not stack else stack[-1]
                w = right - left -1
                res = max(res,h*w)
            stack.append(right)
        return res