from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp1, dp2 = [1] * n, [1] * n
        for i in range(1, n):
            if nums1[i] >= nums1[i - 1]:
                dp1[i] = dp1[i - 1] + 1
            if nums1[i] >= nums2[i - 1]:
                dp1[i] = max(dp1[i], dp2[i - 1] + 1)
            if nums2[i] >= nums2[i - 1]:
                dp2[i] = dp2[i - 1] + 1
            if nums2[i] >= nums1[i - 1]:
                dp2[i] = max(dp2[i], dp1[i - 1] + 1)
            print(dp1)
            print(dp2)
        return max(max(dp1), max(dp2))


S = Solution()

nums1 = [8, 7, 4]
nums2 = [13, 4, 4]
# 4
print(S.maxNonDecreasingLength(nums1, nums2))
