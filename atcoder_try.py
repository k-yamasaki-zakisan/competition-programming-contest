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

from heapq import heapify, heappop, heappush

N, L = map(int, input().split())
A = list(map(int, input().split()))
if sum(A) < L:
    A.append(L - sum(A))
h = A[::-1]
heapify(h)
ans = 0
while 1 < len(h):
    x1 = heappop(h)
    x2 = heappop(h)
    ans += x1 + x2
    heappush(h, x1 + x2)
print(ans)
