from typing import List, Optional

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        max_num = nums[-1]
        set_nums = set(nums)
        ans = -1
        for num in nums:
            cnt = 0
            while num <= max_num:
                if num in set_nums:
                    cnt += 1
                else:
                    break
                num *= num
            if 2 <= cnt:
                ans = max(ans, cnt)
        return ans


S = Solution()
nums = [10, 2, 13, 16, 8, 9, 13]
print(S.longestSquareStreak(nums))
