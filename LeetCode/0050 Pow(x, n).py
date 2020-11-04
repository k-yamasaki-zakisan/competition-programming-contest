# https://leetcode.com/problems/powx-n/
# Runtime: 32 ms, faster than 48.92% of Python3 online submissions for Pow(x, n).
# Memory Usage: 14.2 MB, less than 99.99% of Python3 online submissions for Pow(x, n).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x,n)


# Runtime: 28 ms, faster than 76.43% of Python3 online submissions for Pow(x, n).
# Memory Usage: 14.1 MB, less than 99.99% of Python3 online submissions for Pow(x, n).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        isNegative = n < 0
        n = abs(n)
        while n > 0:
            if n % 2 == 0:
                x *= x
                n /= 2
            else:
                res *= x
                n -= 1
                
        return res if not isNegative else 1 / res