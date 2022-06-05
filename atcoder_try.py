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

from collections import defaultdict

N = int(input())

d = defaultdict(int)
for i in range(1, N + 1):
    j = 2
    while j**2 <= min(i, N):
        if i % j**2 == 0:
            i //= j**2
        else:
            j += 1
    d[i] += 1
ans = 0
for v in d.values():
    ans += v**2
print(ans)
