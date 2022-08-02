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


INF = float("inf")
MOD1 = 10**9 + 7
MOD2 = 998244353

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

MOD2 = 998244353

N = int(input())
A = list(map(int, input().split()))
ans = 0
for m in range(1, N + 1):
    dp = [[[0] * m for _ in range(m + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        ai = A[i] % m
        for j in range(min(m + 1, i + 1)):
            for k in range(m):
                dp[i + 1][j][k] += dp[i][j][k]
                dp[i + 1][j][k] %= MOD2
                if j + 1 <= m:
                    dp[i + 1][j + 1][(k + ai) % m] += dp[i][j][k]
                    dp[i + 1][j + 1][(k + ai) % m] %= MOD2

    ans += dp[N][m][0]
    ans %= MOD2

print(ans)
