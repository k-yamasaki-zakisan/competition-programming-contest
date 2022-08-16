# https://leetcode.com/problems/numbers-with-repeated-digits/
# Runtime: 61 ms, faster than 38.16% of Python3 online submissions for Numbers With Repeated Digits.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Numbers With Repeated Digits.


class Solution:
    def numDupDigitsAtMostN(self, N):
        L = list(map(int, str(N + 1)))
        n = len(L)
        res = sum(9 * perm(9, i) for i in range(n - 1))
        s = set()
        for i, x in enumerate(L):
            for y in range(i == 0, x):
                if y not in s:
                    res += perm(9 - i, n - i - 1)
            if x in s:
                break
            s.add(x)
        return N - res
