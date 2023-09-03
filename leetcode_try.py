from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        from collections import defaultdict

        len_nums = len(nums)
        cnts = [0] * len_nums
        for i in range(len_nums):
            if nums[i] % modulo == k:
                cnts[i] += 1
        for i in range(1, len_nums):
            cnts[i] += cnts[i - 1]
        memo = defaultdict(int)
        for cnt in cnts:
            memo[cnt] += 1
        print(cnts)

        ans = 0
        for key, val in memo.items():
            if key % modulo == k:
                ans += val
            else:
                ans += val - 1
        return ans


S = Solution()
nums = [11, 12, 21, 31]
modulo = 10
k = 1
print(S.countInterestingSubarrays(nums, modulo, k))
# 5
