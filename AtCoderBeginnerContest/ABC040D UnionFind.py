#https://atcoder.jp/contests/abc040/tasks/abc040_d

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

class UnionFindPathCompression():
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1]*n
        self.size = [1]*n

    #findは親を探すメソッド
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
                #ランクの更新
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1


n,m = map(int,input().split())
ufpc = UnionFindPathCompression(n)
aby = [list(map(int, input().split())) for _ in range(m)]
aby = sorted(aby, key=lambda x: -x[2])
q = int(input())
vw = []
for i in range(q):
    v,w = map(int,input().split())
    vw.append([v,w,i])
vw = sorted(vw, key=lambda x: -x[1])
ans = [0]*q
old = 0
for i in range(q):
    v,w,index = vw[i]
    v -= 1
    while old < m and w < aby[old][2]:
        a,b = aby[old][0]-1, aby[old][1]-1
        ufpc.union(a,b)
        old += 1
    ans[index] = ufpc.size[ufpc.find(v)]

for aa in ans:
    print(aa)
