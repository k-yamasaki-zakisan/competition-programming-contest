# https://leetcode.com/problems/flip-string-to-monotone-increasing/
# Runtime: 484 ms, faster than 15.51% of Python3 online submissions for Flip String to Monotone Increasing.
# Memory Usage: 20.1 MB, less than 16.12% of Python3 online submissions for Flip String to Monotone Increasing.

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        S = list(S)
        l_s = len(S)
        zero, one = [0]*l_s, [0]*l_s
        for i, s in enumerate(S):
            if s == '0':
                zero[i] = zero[i-1]+1
                one[i] = one[i-1]
            else:
                zero[i] = zero[i-1]
                one[i] = one[i-1]+1

        ans = min(zero[-1], one[-1])
        for i in range(1, l_s):
            ans = min(ans, one[i-1]+zero[-1]-zero[i-1])
        return ans
