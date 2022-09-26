from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        len_nums = len(nums)
        before = [False] * len_nums
        after = [False] * len_nums
        now_i = k
        if k == 1:
            return [i for i in range(1, len_nums - 1)]
        while now_i < len_nums - k:
            flag = True
            for i in range(now_i - k + 1, now_i):
                if nums[i - 1] < nums[i]:
                    now_i = i + k
                    flag = False
                    break
            if not flag:
                continue
            while now_i < len_nums - k:
                if nums[now_i - 2] < nums[now_i - 1]:
                    now_i = now_i - 1 + k
                    break
                else:
                    before[now_i] = True
                    now_i += 1
        now_i = k
        while now_i < len_nums - k:
            flag = True
            for i in range(now_i + 1, now_i + k):
                if nums[i] > nums[i + 1]:
                    now_i = i
                    flag = False
                    break
            if not flag:
                continue
            while now_i < len_nums - k:
                if nums[now_i + k - 1] > nums[now_i + k]:
                    now_i += k - 1
                    break
                else:
                    after[now_i] = True
                    now_i += 1
        ans = []
        print(before, after)
        for i in range(len_nums):
            if after[i] and before[i]:
                ans.append(i)
        return ans


S = Solution()
nums = [877464, 394689, 51354, 348332, 285490, 570624]
k = 2
print(S.goodIndices(nums, k))
