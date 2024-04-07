import sys
from typing import List

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        self.parents = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
        for s, g, w in edges:
            self.union(s, g)
        p_vals = {}
        for s, g, w in edges:
            p = self.find(s)
            if p in p_vals:
                p_vals[p] = p_vals[p] & w
            else:
                p_vals[p] = w
        ans = []
        for s, g in query:
            p_s, p_g = self.find(s), self.find(g)
            if s == g:
                ans.append(0)
            elif p_s != p_g:
                ans.append(-1)
            else:
                if p_s in p_vals:
                    ans.append(p_vals[p_s])
                else:
                    ans.append(0)
        # print(self.parents, p_vals)
        return ans

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
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
