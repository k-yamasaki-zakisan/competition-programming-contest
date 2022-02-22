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
from math import gcd


def lcm(a, b):
    return int(a * b / gcd(a, b))


N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
dp = [set() for _ in range(N)]
dp[0].add(AB[0])


for i in range(1, N):

    a, b = AB[i]
    for x, y in dp[i - 1]:
        tmp = gcd(x, a), gcd(y, b)
        dp[i].add(tuple(sorted(tmp)))
        tmp = gcd(x, b), gcd(y, a)
        dp[i].add(tuple(sorted(tmp)))

ans = 0
for X, Y in dp[-1]:
    ans = max(ans, lcm(X, Y))
print(ans)
