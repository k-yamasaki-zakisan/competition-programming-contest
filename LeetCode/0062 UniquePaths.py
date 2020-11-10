# https://leetcode.com/problems/unique-paths/
# Runtime: 32 ms, faster than 55.64% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.2 MB, less than 99.99% of Python3 online submissions for Unique Paths.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def combination(n, k):
            import math
            return math.factorial(n) // math.factorial(k) // math.factorial(n - k)
        
        return combination(m-1+n-1,m-1)