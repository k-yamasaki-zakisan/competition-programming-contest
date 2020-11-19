# https://atcoder.jp/contests/abc183/tasks/abc183_f

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def merge(a:dict ,b:dict) -> dict:
    if len(a) < len(b):
        a,b = b,a
    for j in b:
        if j in a:
            a[j] += b[j]
        else:
            a[j] = b[j]
    return a

class UnionFindPathCompression():
    def __init__(self, n, c):
        self.parents = list(range(n))
        self.rank = [1]*n
        self.size = [1]*n
        self.info = [{c[i]:1} for i in range(n)]

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
            if self.rank[px] > self.rank[py]:
                self.parents[py] = px
                self.rank[px] = max(self.rank[px], self.rank[py] + 1)
                self.size[px] += self.size[py]
                self.info[px] = merge(self.info[px], self.info[py])
            else:
                self.parents[px] = py
                self.size[py] += self.size[px]
                self.rank[px] = max(self.rank[py], self.rank[px] + 1)
                self.info[py] = merge(self.info[px], self.info[py])


N,Q = map(int,input().split())
C = list(map(int,input().split()))
ufpc = UnionFindPathCompression(N, C)
Query = [list(map(int,input().split())) for _ in range(Q)]
for x ,a ,b in Query:
    if x == 1:
        ufpc.union(a-1, b-1)
    else:
        r = ufpc.find(a-1)
        if b in ufpc.info[r]:
            print(ufpc.info[r][b])
        else:
            print(0)