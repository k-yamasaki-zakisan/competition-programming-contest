# https://leetcode.com/problems/binary-prefix-divisible-by-5/
# Runtime: 419 ms, faster than 65.07% of Python3 online submissions for Binary Prefix Divisible By 5.
# Memory Usage: 15.1 MB, less than 52.18% of Python3 online submissions for Binary Prefix Divisible By 5.


class Solution:
    def prefixesDivBy5(self, A):
        result = []
        number = 0
        for bit in A:
            number = 2 * number + bit
            result.append(number % 5 == 0)
        return result
