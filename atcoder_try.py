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

from collections import defaultdict

N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())
XY = set()
for _ in range(M):
    X, Y = map(int, input().split())
    XY.add((X, Y))

ans = defaultdict(int)
ans[(0, 0)] = 1
for _ in range(N):
    memo = defaultdict(int)
    for key, val in ans.items():
        ab = (key[0] + A, key[1] + B)
        cd = (key[0] + C, key[1] + D)
        ef = (key[0] + E, key[1] + F)
        if ab not in XY:
            memo[ab] = (memo[ab] + val) % MOD2
        if cd not in XY:
            memo[cd] = (memo[cd] + val) % MOD2
        if ef not in XY:
            memo[ef] = (memo[ef] + val) % MOD2
    ans = memo
print(sum(ans.values()) % MOD2)
