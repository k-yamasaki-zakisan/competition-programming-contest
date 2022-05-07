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

N = int(input())
A = [int(input()) for _ in range(N)]
pos = {}
for i, a in enumerate(A):
    pos[a] = i
a_sort = sorted(A)
ans = 0
for i, a in enumerate(a_sort):
    ans += abs(i - pos[a]) % 2
print(ans // 2)
