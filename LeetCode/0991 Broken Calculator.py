# https://leetcode.com/problems/broken-calculator/
# Runtime: 47 ms, faster than 43.55% of Python3 online submissions for Broken Calculator.
# Memory Usage: 13.8 MB, less than 96.57% of Python3 online submissions for Broken Calculator.


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while startValue < target:
            if target % 2:
                target += 1
            else:
                target //= 2
            ans += 1
        return ans + (startValue - target)
