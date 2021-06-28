# https://atcoder.jp/contests/past201912-open/tasks/past201912_l

import sys
from itertools import combinations
from copy import deepcopy
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


N, M = map(int, input().split())
XYCN = [list(map(int, input().split())) for _ in range(N)]
XYCM = [list(map(int, input().split())) for _ in range(M)]
costs_origin = []
for i in range(N):
    x1, y1, c1 = XYCN[i]
    for j in range(i+1, N):
        if i == j:
            continue
        x2, y2, c2 = XYCN[j]
        cost = ((x2-x1)**2+(y2-y1)**2)**0.5
        if c1 != c2:
            cost *= 10
        costs_origin.append((i, j, cost))
        costs_origin.append((j, i, cost))

ans = float('inf')
for m_cnt in range(M+1):
    for V in combinations(range(M), m_cnt):
        costs = deepcopy(costs_origin)

        for i in range(N):
            x1, y1, c1 = XYCN[i]
            for j in V:
                x2, y2, c2 = XYCM[j]
                cost = ((x2-x1)**2+(y2-y1)**2)**0.5
                if c1 != c2:
                    cost *= 10
                costs.append((i, j+N, cost))
                costs.append((j+N, i, cost))
        for i in V:
            x1, y1, c1 = XYCM[i]
            for j in V:
                if i == j:
                    continue
                x2, y2, c2 = XYCM[j]
                cost = ((x2-x1)**2+(y2-y1)**2)**0.5
                if c1 != c2:
                    cost *= 10
                costs.append((i+N, j+N, cost))
                costs.append((j+N, i+N, cost))

        costs = sorted(costs, key=lambda x: x[2])
        check = [False]*N
        check[0] = True
        ufpc = UnionFindPathCompression(N+M)
        tmp = 0
        for pp, np, cost in costs:
            if ufpc.find(pp) != ufpc.find(np):
                ufpc.union(pp, np)
                tmp += cost
        ans = min(ans, tmp)

print(ans)
