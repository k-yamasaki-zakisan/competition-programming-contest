# https://leetcode.com/problems/largest-component-size-by-common-factor/
# Runtime: 1942 ms, faster than 97.48% of Python3 online submissions for Largest Component Size by Common Factor.
# Memory Usage: 18.8 MB, less than 86.16% of Python3 online submissions for Largest Component Size by Common Factor.

import sys
from typing import List

sys.setrecursionlimit(10**7)


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        num_max = max(nums)
        zip_nums = {num: i for i, num in enumerate(nums)}
        visited = [0] * (num_max + 1)
        N = len(nums)
        UF = UnionFindPathCompression(N)
        for num in range(2, num_max + 1):
            tmp = []
            ori = num
            if 0 < visited[num]:
                continue
            while num <= num_max:
                visited[num] += 1
                if num in zip_nums:
                    tmp.append(zip_nums[num])
                num += ori
            for i_p in range(1, len(tmp)):
                UF.union(tmp[i_p], tmp[i_p - 1])
        for i in range(N):
            UF.find(i)
        return max(UF.size)


class UnionFindPathCompression:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return
        else:
            if self.rank[px] < self.rank[py]:
                self.parents[px] = py
                self.size[py] += self.size[px]
            else:
                self.parents[py] = px
                self.size[px] += self.size[py]
                # ランクの更新
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
