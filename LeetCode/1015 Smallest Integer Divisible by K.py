# https://leetcode.com/problems/smallest-integer-divisible-by-k/
# Runtime: 69 ms, faster than 78.65% of Python3 online submissions for Smallest Integer Divisible by K.
# Memory Usage: 13.8 MB, less than 74.16% of Python3 online submissions for Smallest Integer Divisible by K.


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        cnt = 1
        num = 1
        for _ in range(k):
            s = num % k
            if s == 0:
                return cnt

            num = s * 10 + 1
            cnt += 1
        return -1
