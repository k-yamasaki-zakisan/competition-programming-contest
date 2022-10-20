# https://leetcode.com/problems/n-th-tribonacci-number/
# Runtime: 36 ms, faster than 86.02% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 13.8 MB, less than 59.31% of Python3 online submissions for N-th Tribonacci Number.


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 0 if n == 0 else 1
        i_0, i_1, i_2 = 0, 1, 1
        for _ in range(n - 2):
            i_0, i_1, i_2 = i_1, i_2, i_0 + i_1 + i_2
        return i_2
