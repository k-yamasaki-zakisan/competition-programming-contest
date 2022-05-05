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


from collections import deque

N, M = map(int, input().split())

root = [[] for _ in range(N)]
for _ in range(M):
    a, b = (int(x) for x in input().split())
    root[b - 1].append(a - 1)
    root[a - 1].append(b - 1)

check = [-1] * N

for k in range(N):
    if check[k] != -1:
        continue
    stack = deque([k])
    check[k] = k
    while len(stack) > 0:
        v = stack.popleft()
        for i in root[v]:
            if check[i] == -1:
                check[i] = k
                stack.append(i)
ans = len(set(check)) - 1
print(ans)
