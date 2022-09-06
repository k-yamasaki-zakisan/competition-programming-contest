# from collections import Counter
# import re
# import copy
# import itertools
# from sys import stdin
# from collections import deque
# from copy import copy
# from itertools import combinations
# from bisect import bisect
# import heapq
# import sys
# from collections import defaultdict
# memo = defaultdict(int)

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float("inf")
MOD1 = 10**9 + 7
MOD2 = 998244353

INF = float("inf")

from heapq import heappop, heappush

N, M = map(int, input().split())
A = list(map(int, input().split()))
UV = [list(map(int, input().split())) for _ in range(M)]
root = [[] for _ in range(N)]
memo = [0] * N
for u, v in UV:
    u, v = u - 1, v - 1
    root[u].append(v)
    root[v].append(u)
    memo[u] += A[v]
    memo[v] += A[u]
q = []
for i, m in enumerate(memo):
    heappush(q, (m, i))
visited = [False] * N
ans = -1
while q:
    num, now = heappop(q)
    if visited[now]:
        continue
    ans = max(ans, num)
    visited[now] = True
    for next in root[now]:
        if visited[next]:
            continue
        memo[next] -= A[now]
        heappush(q, (memo[next], next))
print(ans)
