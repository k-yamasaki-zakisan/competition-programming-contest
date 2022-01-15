# https://atcoder.jp/contests/abc235/tasks/abc235_e

import sys
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


N, M, Q = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
ABC = [(0, abc[0]-1, abc[1]-1, abc[2], i) for i, abc in enumerate(ABC)]
UVW = [list(map(int, input().split())) for _ in range(Q)]
UVW = [(1, abc[0]-1, abc[1]-1, abc[2], i) for i, abc in enumerate(UVW)]
root = ABC+UVW
root = sorted(root, key=lambda x: x[3])
ufpc = UnionFindPathCompression(N)
ans = ['']*Q
for r in root:
    f, a, b, c, i = r
    if ufpc.find(a) != ufpc.find(b):
        if f == 1:
            ans[i] = 'Yes'
        else:
            ufpc.union(a, b)
    else:
        if f == 1:
            ans[i] = 'No'
for a in ans:
    print(a)
