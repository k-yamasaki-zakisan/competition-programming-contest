# https://atcoder.jp/contests/zone2021/tasks/zone2021_e

import heapq


def dij(cost, start):
    d = [float('inf')] * (R*C*4)
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


R, C = map(int, input().split())
gr, gc = R-1, C-1
A = [list(map(int, input().split())) for _ in range(R)]
B = [list(map(int, input().split())) for _ in range(R-1)]
cost = [[] for _ in range(R*C*3)]
for y in range(R):
    for x in range(C):
        now_pon = y*C+x
        cost[now_pon].append((2*R*C+C*y+x, 1))
        cost[2*R*C+C*y+x].append((now_pon, 0))
        cost[R*C+C*y+x].append((2*R*C+C*y+x, 0))
        cost[2*R*C+C*y+x].append((R*C+C*y+x, 0))
        if 0 < y:
            cost[R*C+C*y+x].append((R*C+C*(y-1)+x, 1))
        for my, mx in [[1, 0], [0, 1], [0, -1]]:
            h = y + my
            w = x + mx
            next_pon = h*C+w
            if not(0 <= h < R and 0 <= w < C):
                continue
            if my == 1 and mx == 0:
                cost[now_pon].append((next_pon, B[y][x]))
            elif my == 0 and mx == 1:
                cost[now_pon].append((next_pon, A[y][x]))
            elif my == 0 and mx == -1:
                cost[now_pon].append((next_pon, A[h][w]))

dis = dij(cost, 0)
print(dis[R*C-1])
