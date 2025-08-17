class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        tmp = 1
        while tmp <= n:
            if tmp == n:
                return True
            tmp *= 4
        return False
