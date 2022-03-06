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

sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float("inf")
MOD1 = 10**9 + 7
MOD2 = 998244353

N = int(input())
memo = []
ans = 0
for num in range(2, N + 1):
    print(f"? 1 {num}")
    sys.stdout.flush()
    dist = int(input())
    ans = max(ans, dist)
    memo.append((num, dist))

memo = sorted(memo, key=lambda x: -x[1])
ori = memo[0][0]
for num in range(1, N + 1):
    if num == ori:
        continue
    print(f"? {ori} {num}")
    sys.stdout.flush()
    dist = int(input())
    ans = max(ans, dist)
print(f"! {ans}")
