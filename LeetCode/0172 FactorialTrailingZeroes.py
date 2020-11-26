# https://leetcode.com/problems/factorial-trailing-zeroes/
# Runtime: 24 ms, faster than 95.60% of Python3 online submissions for Factorial Trailing Zeroes.
# Memory Usage: 14.3 MB, less than 21.73% of Python3 online submissions for Factorial Trailing Zeroes.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        i = 5
        while i <= n:
            ans += n//i
            i *= 5
        return ans