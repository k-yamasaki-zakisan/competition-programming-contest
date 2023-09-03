from typing import List
from collections import Counter


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans = 0
        tmp = 0
        memo = Counter()
        memo[0] = 1
        for num in nums:
            if num % modulo == k:
                tmp += 1
            tmp %= modulo
            ans += memo[(tmp - k) % modulo]
            memo[tmp] += 1
        return ans
