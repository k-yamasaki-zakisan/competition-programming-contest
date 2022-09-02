# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
# Runtime: 193 ms, faster than 28.22% of Python3 online submissions for Maximum Sum of Two Non-Overlapping Subarrays.
# Memory Usage: 14.4 MB, less than 9.21% of Python3 online submissions for Maximum Sum of Two Non-Overlapping Subarrays.

from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        fir, sec = [], []
        len_nums = len(nums)
        tmp_f = 0
        for i in range(len_nums):
            tmp_f += nums[i]
            if firstLen <= i:
                tmp_f -= nums[i - firstLen]
            if firstLen - 1 <= i:
                fir.append([tmp_f, i - firstLen + 1, i])
        tmp_s = 0
        for i in range(len_nums):
            tmp_s += nums[i]
            if secondLen <= i:
                tmp_s -= nums[i - secondLen]
            if secondLen - 1 <= i:
                sec.append([tmp_s, i - secondLen + 1, i])
        sec = sorted(sec, key=lambda x: -x[0])
        ans = -1
        for f_n, f_f, f_g in fir:
            for s_n, s_f, s_g in sec:
                if s_g < f_f or f_g < s_f:
                    ans = max(ans, f_n + s_n)
                    break
        return ans
