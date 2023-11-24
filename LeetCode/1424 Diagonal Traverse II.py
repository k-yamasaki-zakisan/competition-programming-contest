from typing import List
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        H = len(nums)
        tmp = defaultdict(list)
        for h, num in enumerate(nums):
            for w in range(len(num)):
                tmp[h + w].append([w, h])
        tmp = sorted(tmp.items())
        ans = []
        for key, vals in tmp:
            vals.sort()
            for w, h in vals:
                ans.append(nums[h][w])
        return ans
