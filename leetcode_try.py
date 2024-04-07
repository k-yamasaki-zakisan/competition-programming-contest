from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        from bisect import bisect_left

        n = len(nums)
        nums.sort()
        print(nums)
        if n == 1:
            return abs(nums[0] - k)
        if nums[n // 2] == k:
            return 0
        mid_i = bisect_left(nums, k)
        print(mid_i)
        ans = 0
        if mid_i <= n // 2:
            for i in range(mid_i, n // 2 + 1):
                ans += nums[i] - k
        else:
            for i in range(n // 2, mid_i):
                ans += k - nums[i]

        return ans


S = Solution()
nums = [98, 52]
k = 82
print(S.minOperationsToMakeMedianK(nums, k))
# 10
