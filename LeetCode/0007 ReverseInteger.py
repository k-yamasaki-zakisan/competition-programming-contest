# https://leetcode.com/problems/reverse-integer/
# Runtime: 32 ms, faster than 63.53% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14.2 MB, less than 99.99% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self, x: int) -> int:
        max_32 = 2**31-1
        if abs(x) > max_32:
            return 0
        if x < 0:
            reverse_int = -int(str(abs(x))[::-1])
        else:
            reverse_int = int(str(x)[::-1])
        if abs(reverse_int) > max_32:
            return 0
        else:
            return reverse_int