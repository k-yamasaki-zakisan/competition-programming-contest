# https://atcoder.jp/contests/code-festival-2014-morning-easy/tasks/code_festival_morning_easy_c

import heapq
INF = float('inf')

N, M = map(int, input().split())
S, T = map(int, input().split())
S, T = S-1, T-1
XYD = [list(map(int, input().split())) for _ in range(M)]
 
def dij(cost, start):
    d = [INF] * N # 最短距離
    d[start] = 0
 
    q = [(d[start], start)] # min-heap, (距離, 頂点)
    heapq.heapify(q)
    while q:
        du, u = heapq.heappop(q) # 最短距離とその頂点
        if d[u] < du:
            continue
        for v, weight in cost[u]:
            if du + weight < d[v]:
                d[v] = du + weight
                heapq.heappush(q, (d[v], v))
    return d
 
 
# コストテーブルの作成
cost = [[] for _ in range(N)]
for i, j, k in XYD:
    cost[i - 1].append((j - 1, k))
    cost[j - 1].append((i - 1, k))

d1 = dij(cost, S)
for i in range(N):
    if i == T or i == S:
        continue
    d2 = dij(cost, i)
    if d1[i] == d2[T] and d1[i] != INF and d2 != INF:
        print(i+1)
        exit()
 
print(-1)