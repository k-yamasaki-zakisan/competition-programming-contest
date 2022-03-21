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
for a in range(1, 100):
    aa = pow(3, a)
    for b in range(1, 100):
        bb = pow(5, b)
        if aa + bb == N:
            print(a, b)
            exit()
        elif N < aa + bb:
            break
print(-1)
