# https://atcoder.jp/contests/abc237/tasks/abc237_e

import heapq
import sys
sys.stdin.readline


def dij(cost, start):
    dp = [-float('inf')] * N
    dp[start] = 0

    query = [(dp[start], start)]
    heapq.heapify(query)
    while query:
        now_c, now = heapq.heappop(query)
        now_c = -now_c
        for next, weight in cost[now]:
            if dp[next] < dp[now] + weight:
                dp[next] = dp[now] + weight
                heapq.heappush(query, (-weight, next))
        # print(query)
    return dp


N, M = map(int, input().split())
H = list(map(int, input().split()))
UV = [list(map(int, input().split())) for _ in range(M)]
cost = [[] for _ in range(N)]
for u, v in UV:
    u, v = u-1, v-1
    if H[u] == H[v]:
        cost[v].append((u, 0))
        cost[u].append((v, 0))
    elif H[u] < H[v]:
        cost[v].append((u, H[v]-H[u]))
        cost[u].append((v, -2*abs(H[v]-H[u])))
    else:
        cost[u].append((v, H[u]-H[v]))
        cost[v].append((u, -2*abs(H[v]-H[u])))
result = dij(cost, 0)
print(max(result))
