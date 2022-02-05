# https://atcoder.jp/contests/abc238/tasks/abc238_e

import sys
sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


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


N, Q = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(Q)]
ufpc = UnionFindPathCompression(N+1)
for l, r in LR:
    ufpc.union(l-1, r)
if ufpc.find(0) == ufpc.find(N):
    print('Yes')
else:
    print('No')
