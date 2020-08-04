#https://atcoder.jp/contests/abc120/tasks/abc120_d

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

class UnionFindPathCompression():
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1]*n
        self.group_size = [1]*n

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
                self.group_size[py] += self.group_size[px]
            else:
                self.parents[py] = px
                self.group_size[px] += self.group_size[py]
                #ランクの更新
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
                
n,m = map(int,input().split())
ufpc = UnionFindPathCompression(n)
query = []
for i in range(m):
    a, b = (int(x) for x in input().split())
    a,b = a-1, b-1
    query.append([a,b])

ans = [0]*m
ans[m-1] = n*(n-1)//2
#queryを後ろから発行してunionfind
for i in range(m-2, -1, -1):
    a,b = query[i+1][0], query[i+1][1]
    if ufpc.find(a) == ufpc.find(b):
        ans[i] = ans[i+1]
    else:
        #親のサイズで不便さを計算
        ans[i] = ans[i+1] - ufpc.group_size[ufpc.parents[a]] * ufpc.group_size[ufpc.parents[b]]

    ufpc.union(a,b)
for aa in ans:
    print(aa)
