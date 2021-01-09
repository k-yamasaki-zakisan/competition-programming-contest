# https://leetcode.com/problems/valid-perfect-square/
# Runtime: 28 ms, faster than 82.05% of Python3 online submissions for Valid Perfect Square.
# Memory Usage: 14.3 MB, less than 33.27% of Python3 online submissions for Valid Perfect Square.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = int(num**0.5)
        return i**2 == num
