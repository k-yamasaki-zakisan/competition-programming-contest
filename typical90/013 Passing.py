# https://atcoder.jp/contests/typical90/tasks/typical90_m

import heapq


def dij(cost, start):
    d = [float('inf')] * N  # 最短距離
    d[start] = 0

    q = [(d[start], start)]  # min-heap, (距離, 頂点)
    heapq.heapify(q)
    while q:
        du, u = heapq.heappop(q)  # 最短距離とその頂点
        if d[u] < du:
            continue
        for v, weight in cost[u]:
            if du + weight < d[v]:
                d[v] = du + weight
                heapq.heappush(q, (d[v], v))
    return d


N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
cost = [[] for _ in range(N)]
for a, b, c in ABC:
    a, b = a-1, b-1
    cost[a].append((b, c))
    cost[b].append((a, c))

d1 = dij(cost, 0)
d2 = dij(cost, N-1)

print(d1[-1])
for i in range(1, N-1):
    print(d1[i]+d2[i])
print(d1[-1])
