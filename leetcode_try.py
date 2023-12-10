from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        from bisect import bisect_left

        n = len(nums)
        max_num = max(nums)
        counts = [0] * n
        for i in range(n):
            if max_num == nums[i]:
                counts[i] += 1
        for i in range(1, n):
            counts[i] += counts[i - 1]
        ans = 0
        print(counts)
        for i in range(n):
            if nums[i] == max_num:
                target_cnt = counts[i] + (k - 1)
            else:
                target_cnt = counts[i] + k
            j = bisect_left(counts, target_cnt)
            # print(i, j)
            if j < n:
                ans += n - j
        return ans


S = Solution()
nums = [1, 3, 2, 3, 3]
k = 2
print(S.countSubarrays(nums, k))
# 10
