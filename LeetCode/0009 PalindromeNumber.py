# https://leetcode.com/problems/palindrome-number/

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