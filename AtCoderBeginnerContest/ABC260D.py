# https://atcoder.jp/contests/abc260/tasks/abc260_d

import sys
from bisect import bisect_left

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


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


N, K = map(int, input().split())
P = list(map(int, input().split()))
P = [p - 1 for p in P]
ufpc = UnionFindPathCompression(N)
yama = []
eat = {}
for i, p in enumerate(P):
    if len(yama) == 0 or yama[-1] < p:
        yama.append(p)
    else:
        idx = bisect_left(yama, p)
        n = yama[idx]
        ufpc.union(n, p)
        yama[idx] = p

    if ufpc.size[ufpc.find(p)] == K:
        eat[ufpc.find(p)] = i + 1
        idx = bisect_left(yama, p)
        del yama[idx]

ans = [-1] * N
for i in range(N):
    p = ufpc.find(i)
    if p not in eat:
        print(-1)
    else:
        print(eat[p])
