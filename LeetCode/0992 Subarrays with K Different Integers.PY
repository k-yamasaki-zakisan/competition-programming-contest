# https://leetcode.com/problems/subarrays-with-k-different-integers/
# Runtime: 478 ms, faster than 95.80% of Python3 online submissions for Subarrays with K Different Integers.
# Memory Usage: 16.7 MB, less than 82.55% of Python3 online submissions for Subarrays with K Different Integers.

from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], K: int) -> int:
        freq = {}
        start = 0
        start_k = 0
        res = 0
        for i, x in enumerate(nums):
            freq[x] = freq.get(x, 0) + 1
            if len(freq) == K + 1:
                del freq[nums[start_k]]
                start_k += 1
                start = start_k
            if len(freq) == K:
                while freq[nums[start_k]] > 1:
                    freq[nums[start_k]] -= 1
                    start_k += 1
                res += start_k - start + 1
        return res
