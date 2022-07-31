# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
# Runtime: 1170 ms, faster than 94.90% of Python3 online submissions for Minimum Number of K Consecutive Bit Flips.
# Memory Usage: 17 MB, less than 92.55% of Python3 online submissions for Minimum Number of K Consecutive Bit Flips.

from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        len_nums = len(nums)
        memo = [0] * len_nums
        cnt = 0
        ans = 0
        for i in range(len_nums - k + 1):
            cnt += memo[i]
            if (nums[i] + cnt) % 2 == 0:
                if i + k < len_nums:
                    memo[i + k] -= 1
                cnt += 1
                ans += 1
        for i in range(len_nums - k + 1, len_nums):
            cnt += memo[i]
            if (nums[i] + cnt) % 2 == 0:
                return -1
        return ans
