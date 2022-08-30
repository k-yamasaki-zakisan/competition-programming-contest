from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        point = [-1] * 501
        for i, num in enumerate(nums):
            point[num] = i
        len_nums = len(nums)
        ans = 0
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                diff = nums[j] - nums[i]
                t = nums[i]
                cnt = 0
                while 0 <= t <= 500 and point[t] != -1:
                    print(t, diff, i, j)
                    cnt += 1
                    t += diff
                ans = max(ans, cnt)
        return ans


S = Solution()
nums = [3, 6, 9, 12]
print(S.longestArithSeqLength(nums))
