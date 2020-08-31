#https://atcoder.jp/contests/abc065/tasks/arc076_b

#最小全域技問題(UnionFindと貪欲の合わせ技)
import sys
input = sys.stdin.readline
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
                #ランクの更新
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1

N = int(input())
town = [[i]+list(map(int,input().split())) for i in range(N)]
root = []
#x軸の小さい順
town = sorted(town, key=lambda x: x[1])
for i in range(1,N):
    px,nx = town[i-1][1], town[i][1]
    root.append([town[i-1][0], town[i][0], nx-px])
#y軸の小さい順
town = sorted(town, key=lambda x: x[2])
for i in range(1,N):
    py,ny = town[i-1][2], town[i][2]
    root.append([town[i-1][0], town[i][0], ny-py])
#コストの少ない順
root = sorted(root, key=lambda x: x[2])
ufpc = UnionFindPathCompression(N)
ans = 0
for pp,np,cost in root:
    if ufpc.find(pp) != ufpc.find(np):
        ufpc.union(pp,np)
        ans += cost
        #print(pp,np,cost,ans)
print(ans)
