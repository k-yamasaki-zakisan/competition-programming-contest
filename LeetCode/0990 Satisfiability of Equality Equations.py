# https://leetcode.com/problems/satisfiability-of-equality-equations/
# Runtime: 52 ms, faster than 84.31% of Python3 online submissions for Satisfiability of Equality Equations.
# Memory Usage: 14 MB, less than 66.88% of Python3 online submissions for Satisfiability of Equality Equations.

from typing import List

CHAR_ID = {chr(ord("a") + i): i for i in range(26)}


class Solution:
    def __init__(self):
        self.parents = list(range(26))
        self.rank = [1] * 26
        self.size = [1] * 26

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

    def equationsPossible(self, equations: List[str]) -> bool:
        for eq in equations:
            if eq[1] == eq[2]:
                self.union(CHAR_ID[eq[0]], CHAR_ID[eq[3]])
        for eq in equations:
            if eq[1] != eq[2]:
                if self.find(CHAR_ID[eq[0]]) == self.find(CHAR_ID[eq[3]]):
                    return False
        return True
