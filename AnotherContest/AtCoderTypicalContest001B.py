#https://atcoder.jp/contests/atc001/tasks/unionfind_a

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

class UnionFindPathCompression():
    def __init__(self, n):
        self.parents = list(range(n))

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
            self.parents[py] = px


n,m = map(int,input().split())
ufpc = UnionFindPathCompression(n)
for _ in range(m):
    p, a, b = (int(x) for x in input().split())
    if p == 0:
        ufpc.union(a,b)
        #print(ufpc.parents)
    if p == 1:
        if ufpc.find(a) == ufpc.find(b):
            print('Yes')
        else:
            print('No')
