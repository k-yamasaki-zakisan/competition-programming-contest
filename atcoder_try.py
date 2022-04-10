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
S = input()
X = input()

X = X[::-1]
S = S[::-1]

E = {0}
for x, s in zip(X, S):
    F = E
    s = int(s)
    if x == "T":
        E = {a for a in range(7) if ((10 * a) % 7 in F) or ((10 * a + s) % 7 in F)}
    else:
        E = {a for a in range(7) if ((10 * a) % 7 in F) and ((10 * a + s) % 7 in F)}
print("Takahashi" if 0 in E else "Aoki")
