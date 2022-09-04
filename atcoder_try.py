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

N, M = map(int, input().split())
A = list(map(int, input().split()))
dp = [[-INF] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(N + 1):
        if j == 0:
            dp[i][0] = 0
        elif j <= i:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + A[i - 1] * j)
print(dp[N][M])
