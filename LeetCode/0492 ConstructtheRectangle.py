# https://leetcode.com/problems/construct-the-rectangle/
# Runtime: 28 ms, faster than 92.22% of Python3 online submissions for Construct the Rectangle.
# Memory Usage: 14.4 MB, less than 10.00% of Python3 online submissions for Construct the Rectangle.

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ans = [area, 1]
        for i in range(2, int(area**0.5)+1):
            if area % i == 0:
                ans = [area // i, i]
        return ans
