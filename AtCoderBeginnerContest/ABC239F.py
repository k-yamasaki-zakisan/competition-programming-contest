# https://atcoder.jp/contests/abc239/tasks/abc239_f

import sys
from collections import defaultdict

sys.stdin.readline
sys.setrecursionlimit(10**7)
INF = float("inf")


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


N, M = map(int, input().split())
D = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
if sum(D) != (N - 1) * 2:
    print(-1)
    exit()
uf = UnionFindPathCompression(N)
for a, b in AB:
    a, b = a - 1, b - 1
    if uf.find(a) == uf.find(b):
        print(-1)
        exit()
    uf.union(a, b)
    D[a] -= 1
    D[b] -= 1

group = [uf.find(i) for i in range(N)]
dic = defaultdict(list)
for i, g in enumerate(group):
    dic[g] += [i] * D[i]
# print(dic)
remain = list(dic.values())
remain.sort(key=lambda x: len(x))
L = len(remain)
now = L - 1
ans = []
for i in range(L - 2, -1, -1):
    if len(remain[i]) == 0 or i == now:
        break
    node1 = remain[i].pop()
    node2 = remain[now].pop()
    ans.append((node1 + 1, node2 + 1))
    while i <= now and len(remain[now]) == 0:
        now -= 1

n = 0
for re in remain:
    n = max(n, len(re))

if len(ans) == N - M - 1 and n == 0:
    for a in ans:
        print(*a)
else:
    print(-1)
# print(remain, ans)
