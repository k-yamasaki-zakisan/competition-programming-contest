# https://atcoder.jp/contests/typical90/tasks/typical90_bp

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


N = int(input())
Q = int(input())
TXYV = [list(map(int, input().split())) for _ in range(Q)]

N_sum_list = [0]*(N-1)
for t, x, y, v in TXYV:
    x, y = x-1, y-1
    if t == 0:
        N_sum_list[x] = v

N_potential = [0]*N
for i in range(N-1):
    N_potential[i+1] = N_sum_list[i] - N_potential[i]

ufpc = UnionFindPathCompression(N)
for t, x, y, v in TXYV:
    x, y = x-1, y-1
    if t == 0:
        ufpc.union(x, y)
    else:
        if ufpc.find(x) != ufpc.find(y):
            print('Ambiguous')
        elif (x + y) % 2 == 0:
            print(v + N_potential[y] - N_potential[x])
        else:
            print(N_potential[x] + N_potential[y] - v)
