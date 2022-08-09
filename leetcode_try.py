from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        abs_nums = [abs(num) for num in nums]
        abs_nums.sort()
        ans = sum(nums)
        for i in range(min(k, len(nums))):
            if nums[i] < 0:
                ans += 2 * abs(nums[i])
            else:
                cnt = k - i
                if cnt % 2:
                    ans -= abs_nums[0] * 2
                return ans
        if len(nums) < k:
            ans -= abs_nums[0] * 2
        return ans


stones = [3, 5, 1, 2, 6]
k = 3
S = Solution()
print(S.mergeStones(stones, k))
