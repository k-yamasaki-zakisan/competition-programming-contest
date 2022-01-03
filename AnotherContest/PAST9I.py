# https://atcoder.jp/contests/past202112-open/tasks/past202112_i

import heapq


def dij(cost, start):
    d = [float('inf')] * len(zahyo)
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


N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

zahyo = [1, N]
for a, b, c in ABC:
    zahyo.append(a)
    zahyo.append(b)
*XS, = set(zahyo)
XS.sort()
zahyo = {e: i for i, e in enumerate(XS)}

cost = [[] for _ in range(len(zahyo))]
for a, b, c in ABC:
    za, zb = zahyo[a], zahyo[b]
    cost[za].append((zb, c))
    cost[zb].append((za, c))
for i in range(1, len(XS)):
    c = XS[i]-XS[i-1]
    cost[i-1].append((i, c))
    cost[i].append((i-1, c))
d = dij(cost, 0)
print(d[-1])
