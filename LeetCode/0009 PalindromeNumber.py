# https://leetcode.com/problems/palindrome-number/
# Runtime: 72 ms, faster than 34.41% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Palindrome Number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        len_x = len(x)
        i = 0
        while i < len_x//2:
            if x[i] != x[len_x-i-1]:
                return False
            i += 1
        return True