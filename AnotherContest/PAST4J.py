# https://atcoder.jp/contests/past202010-open/tasks/past202010_j
# ダイグストラ法　コストテーブルの正しい作成が肝

import heapq
def dij(cost, start):
    d = [float('inf')] * (N+6)
    d[start] = 0
 
    q = [(d[start], start)]
    heapq.heapify(q)
    while q:
        du, u = heapq.heappop(q)
        if d[u] < du:
            continue
        for v, weight in cost[u]:
            if du + weight < d[v]:
                d[v] = du + weight
                heapq.heappush(q, (d[v], v))
    return d

N,M = map(int,input().split())
XAB,XAC,XBC = map(int,input().split())
S = list(input())
ABC = [list(map(int, input().split())) for _ in range(M)]
cost = [[] for _ in range(N+6)]
for a, b, c in ABC:
    cost[a-1].append((b-1, c))
    cost[b-1].append((a-1, c))
# N=Ainm N+1=Bin N+2=Cin N+3=Aout N+4=Bout N+5=Cout
cost[N].append((N+4,XAB))
cost[N].append((N+5,XAC))
cost[N+1].append((N+3,XAB))
cost[N+1].append((N+5,XBC))
cost[N+2].append((N+3,XAC))
cost[N+2].append((N+4,XBC))
for i,val in enumerate(S):
    if val == 'A':
        cost[i].append((N,0))
        cost[N+3].append((i,0))
    elif val == 'B':
        cost[i].append((N+1,0))
        cost[N+4].append((i,0))
    elif val == 'C':
        cost[i].append((N+2,0))
        cost[N+5].append((i,0))
result = dij(cost, 0)
print(result[N-1])