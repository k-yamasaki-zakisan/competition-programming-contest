from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 0, max(nums)
        while 1 < r - l:
            mid = (l + r) // 2
            tmp = 0
            for num in nums:
                while mid < num:
                    num //= 2
                    tmp += 1
            if tmp <= maxOperations:
                r = mid
            else:
                l = mid
        return r


S = Solution()
n = 5
k = 2
print(S.findTheWinner(n, k))
# 10
