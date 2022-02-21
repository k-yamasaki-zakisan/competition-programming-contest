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

# import sys

# sys.stdin.readline
# sys.setrecursionlimit(10**7)

INF = float("inf")
MOD = 10**9 + 7

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
dp = [[0] * W for _ in range(H)]
dp_tate = [[0] * W for _ in range(H)]
dp_yoko = [[0] * W for _ in range(H)]
dp_nana = [[0] * W for _ in range(H)]
dp[0][0] = dp_tate[0][0] = dp_yoko[0][0] = dp_nana[0][0] = 1
for h in range(1, H):
    if S[h][0] == "#":
        break

    if h == 1:
        dp[h][0] = 1

    else:
        dp[h][0] = (dp[h - 1][0] * 2) % MOD
    dp_tate[h][0] = dp_yoko[h][0] = dp_nana[h][0] = dp[h][0]
for w in range(1, W):
    if S[0][w] == "#":
        break

    if w == 1:
        dp[0][w] = 1
    else:
        dp[0][w] = (dp[0][w - 1] * 2) % MOD
    dp_tate[0][w] = dp_yoko[0][w] = dp_nana[0][w] = dp[0][w]

for h in range(1, H):
    for w in range(1, W):
        if S[h][w] == "#":
            continue
        dp[h][w] = (dp_tate[h - 1][w] + dp_yoko[h][w - 1] + dp_nana[h - 1][w - 1]) % MOD
        dp_tate[h][w] = (dp[h][w] + dp_tate[h - 1][w]) % MOD
        dp_yoko[h][w] = (dp[h][w] + dp_yoko[h][w - 1]) % MOD
        dp_nana[h][w] = (dp[h][w] + dp_nana[h - 1][w - 1]) % MOD
print(dp[H - 1][W - 1])
