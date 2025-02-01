from typing import List
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


class UnionFindPathCompression:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1] * n
        self.group_size = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # 親を探す p = parentの意味
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return
        else:
            if self.rank[px] < self.rank[py]:
                self.parents[px] = py
                self.group_size[py] += self.group_size[px]
            else:
                self.parents[py] = px
                self.group_size[px] += self.group_size[py]
                # ランクの更新
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ufpc = UnionFindPathCompression(len(edges) + 1)
        for s, t in edges:
            if ufpc.find(s) == ufpc.find(t):
                return [s, t]
            ufpc.union(s, t)
        raise Exception
