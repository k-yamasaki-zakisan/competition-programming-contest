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

MOD = 998244353

n = int(input())
a = list(map(int, input().split()))
cum = [0] * (n + 1)

for i in range(n - 2, -1, -1):
    ans = cum[i + 1] - cum[i + a[i] + 1] + a[i] + 1
    ans %= MOD
    ans *= pow(a[i], MOD - 2, MOD)
    ans %= MOD
    cum[i] = ans + cum[i + 1]

print((cum[0] - cum[1]) % MOD)
