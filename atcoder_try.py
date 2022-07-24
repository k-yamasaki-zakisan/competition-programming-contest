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


N, C = map(int, input().split())
TA = [list(map(int, input().split())) for _ in range(N)]
X = C
dp = [[0, 1] for _ in range(30)]
for t, a in TA:
    nX = 0
    for i in range(30):
        for j in range(2):
            if t == 1:
                dp[i][j] &= (a >> i) % 2
            if t == 2:
                dp[i][j] |= (a >> i) % 2
            if t == 3:
                dp[i][j] ^= (a >> i) % 2
        nX += (dp[i][(X >> i) % 2]) * (1 << i)
    X = nX
    print(X)
