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

sys.setrecursionlimit(10**7)

INF = float("inf")
MOD1 = 10**9 + 7
MOD2 = 998244353

INF = float("inf")

N = int(input())
A = list(map(int, input().split()))

dp1 = 0
dp2 = INF
for i in range(N):
    a = A[i]
    dp1, dp2 = dp2, min(dp1, dp2) + a

ans = min(dp1, dp2)

dp1 = INF
dp2 = A[-1]
for i in range(N - 1):
    a = A[i]
    dp1, dp2 = dp2, min(dp1, dp2) + a

ans = min(ans, dp1, dp2)

print(ans)
