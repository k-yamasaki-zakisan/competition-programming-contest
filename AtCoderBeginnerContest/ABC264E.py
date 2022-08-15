import sys

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


INF = float("inf")
MOD1 = 10**9 + 7
MOD2 = 998244353

N, M, E = map(int, input().split())
UV = [list(map(int, input().split())) for _ in range(E)]
Q = int(input())
X = [int(input()) for _ in range(Q)]
x_set = set(X)
UT = UnionFindPathCompression(N + M)
cnt = 0
denki = set([i for i in range(N, N + M)])

for i in range(E):
    if i + 1 not in x_set:
        u, v = UV[i][0] - 1, UV[i][1] - 1
        u_p, v_u = UT.find(u), UT.find(v)
        if u_p not in denki and v_u in denki:
            cnt += UT.size[u_p]
        elif u_p in denki and v_u not in denki:
            cnt += UT.size[v_u]
        UT.union(u, v)
        if (u_p not in denki and v_u in denki) or (u_p in denki and v_u not in denki):
            u_p = UT.find(u)
            denki.add(u_p)

ans = [cnt]
for i in X[::-1]:
    u, v = UV[i - 1][0] - 1, UV[i - 1][1] - 1
    u_p, v_u = UT.find(u), UT.find(v)
    if u_p not in denki and v_u in denki:
        cnt += UT.size[u_p]
    elif u_p in denki and v_u not in denki:
        cnt += UT.size[v_u]
    UT.union(u, v)
    if (u_p not in denki and v_u in denki) or (u_p in denki and v_u not in denki):
        u_p = UT.find(u)
        denki.add(u_p)

    ans.append(cnt)
ans.pop()
for a in ans[::-1]:
    print(a)
