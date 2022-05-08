# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# Runtime: 472 ms, faster than 26.30% of Python3 online submissions for Subarray Sums Divisible by K.
# Memory Usage: 18.9 MB, less than 68.58% of Python3 online submissions for Subarray Sums Divisible by K.

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        nums_memo = defaultdict(int)
        nums_memo[0] = 1
        ans = 0
        tmp = 0
        for num in nums:
            tmp = (tmp + num) % k
            ans += nums_memo[tmp]
            nums_memo[tmp] += 1
        return ans
