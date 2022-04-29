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

from collections import deque


class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for i in range(n)]

    def add_edge(self, fr, to, cap, op):
        self.g[fr].append([to, cap, len(self.g[to]), 1 & op])
        self.g[to].append([fr, 0, len(self.g[fr]) - 1, 0])

    def bfs(self, s):
        level = [-1] * self.n
        deq = deque()
        level[s] = 0
        deq.append(s)
        while deq:
            v = deq.popleft()
            for e in self.g[v]:
                if e[1] > 0 and level[e[0]] < 0:
                    level[e[0]] = level[v] + 1
                    deq.append(e[0])
        self.level = level

    def dfs(self, v, t, f):
        if v == t:
            return f
        es = self.g[v]
        level = self.level
        for i in range(self.it[v], len(self.g[v])):
            e = es[i]
            if e[1] > 0 and level[v] < level[e[0]]:
                d = self.dfs(e[0], t, min(f, e[1]))
                if d > 0:
                    e[1] -= d
                    self.g[e[0]][e[2]][1] += d
                    self.it[v] = i
                    return d
        self.it[v] = len(self.g[v])
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                break
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, 10**9 + 7)
                if f > 0:
                    flow += f
                else:
                    break
        return flow


N, A, B = map(int, input().split())
dinic = Dinic(N)
dinic2 = Dinic(N)
for i in range(A):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    dinic.add_edge(x, y, 400, 0)
    dinic2.add_edge(x, y, 400, 0)
for i in range(B):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    dinic.add_edge(x, y, 1, 1)
f = dinic.max_flow(0, N - 1)
f2 = dinic2.max_flow(0, N - 1)

print(A + B - (f - f2))
