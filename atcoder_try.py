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

from heapq import heappop, heappush

N, L, R = map(int, input().split())
A = list(map(int, input().split()))
sum_a = sum(A)
ans = sum_a
memo = []
ruiseki = [0]
for i, a in enumerate(A):
    ruiseki.append(ruiseki[-1] + a)
    heappush(memo, [sum_a - ruiseki[-1] + (i + 1) * L, i])
ans = min(ans, memo[0][0])
ruiseki_r = [0]
for i in range(N - 1, -1, -1):
    a = A[i]
    ruiseki_r.append(ruiseki_r[-1] + a)
    ans = min(ans, sum_a - ruiseki_r[-1] + (N - i) * R)
    while len(memo) and i <= memo[0][1]:
        heappop(memo)
    if len(memo):
        ans = min(ans, memo[0][0] - ruiseki_r[-1] + (N - i) * R)

print(ans)
