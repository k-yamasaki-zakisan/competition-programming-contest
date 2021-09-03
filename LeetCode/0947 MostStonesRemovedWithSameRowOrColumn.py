# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# Runtime: 150 ms, faster than 73.72% of Python3 online submissions for Most Stones Removed with Same Row or Column.
# Memory Usage: 15.2 MB, less than 44.10% of Python3 online submissions for Most Stones Removed with Same Row or Column.

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        import sys
        from collections import defaultdict
        sys.setrecursionlimit(10 ** 7)
        N = len(stones)
        ufpc = UnionFindPathCompression(N)
        x_memo = defaultdict(int)
        y_memo = defaultdict(int)
        for i, xy in enumerate(stones):
            x, y = xy
            if x in x_memo:
                ufpc.union(x_memo[x], i)
            if y in y_memo:
                ufpc.union(y_memo[y], i)
            x_memo[x] = i
            y_memo[y] = i
        parents = set()
        for i in range(N):
            parents.add(ufpc.find(i))
        ans = 0
        for p in parents:
            ans += (ufpc.size[p]-1)
        return ans


class UnionFindPathCompression():
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1]*n
        self.size = [1]*n

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
