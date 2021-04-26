# https://atcoder.jp/contests/typical90/tasks/typical90_l

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


class UnionFindPathCompression():
    def __init__(self, n: int):
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


H, W = map(int, input().split())
MAXNUM = H*W
Q = int(input())
Queries = [list(map(int, input().split())) for _ in range(Q)]
ufpc = UnionFindPathCompression(MAXNUM)
check_red = [False]*(MAXNUM)
for query in Queries:
    if query[0] == 1:
        q, h, w = query
        h, w = h-1, w-1
        num = h*W+w
        check_red[num] = True

        if 0 < w and check_red[num-1]:
            ufpc.union(num, num-1)
        if w < W-1 and check_red[num+1]:
            ufpc.union(num, num+1)
        num_bottom = (h-1)*W+w
        if 0 < h and check_red[num_bottom]:
            ufpc.union(num, num_bottom)
        num_up = (h+1)*W+w
        if h < H-1 and check_red[num_up]:
            ufpc.union(num, num_up)
    else:
        q, h1, w1, h2, w2 = query
        h1, w1 = h1-1, w1-1
        num1 = h1*W+w1
        h2, w2 = h2-1, w2-1
        num2 = h2*W+w2
        is_reds = (check_red[num1] and check_red[num2])
        if not is_reds:
            print('No')
            continue

        if ufpc.find(num1) == ufpc.find(num2):
            print('Yes')
        else:
            print('No')
