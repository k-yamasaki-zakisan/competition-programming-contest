# https://leetcode.com/problems/water-and-jug-problem/
# Runtime: 28 ms, faster than 84.70% of Python3 online submissions for Water and Jug Problem.
# Memory Usage: 14.4 MB, less than 32.82% of Python3 online submissions for Water and Jug Problem.

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x > y:
            x, y = y, x

        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        ans = gcd(y, x)
        if ans == 0:
            return z == 0
        return (x+y) >= z and z % ans == 0
