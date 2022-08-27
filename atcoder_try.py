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

N = int(input())
TXA = [list(map(int, input().split())) for _ in range(N)]
X = [0] * (TXA[-1][0] + 1)
A = [0] * (TXA[-1][0] + 1)
for t, x, a in TXA:
    X[t] = x
    A[t] = a

dp = [[-INF] * (TXA[-1][0] + 1) for _ in range(5)]
dp[0][0] = 0
for t in range(1, (TXA[-1][0] + 1)):
    for i in range(5):
        dp[i][t] = dp[i][t - 1]
        if i != 0:
            dp[i][t] = max(dp[i][t], dp[i - 1][t - 1])
        if i != 4:
            dp[i][t] = max(dp[i][t], dp[i + 1][t - 1])
    dp[X[t]][t] += A[t]
print(max(dp[i][-1] for i in range(5)))
