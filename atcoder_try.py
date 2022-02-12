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
MOD = 10**9 + 7
INF = float("inf")


class UnionFindPathCompression:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return
        else:
            if self.rank[px] < self.rank[py]:
                self.parents[px] = py
                self.size[py] += self.size[px]
            else:
                self.parents[py] = px
                self.size[px] += self.size[py]
                # ランクの更新
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1


N = int(input())
S1 = list(input())
S2 = list(input())
base = ord("A")
nums = [str(num) for num in range(10)]
ufpc = UnionFindPathCompression(26)
checked = set()
alfs = set()
for i in range(N):
    if S1[i] not in nums and S2[i] not in nums:
        ufpc.union(ord(S1[i]) - base, ord(S2[i]) - base)
    elif S1[i] in nums and S2[i] not in nums:
        checked.add(ord(S2[i]) - base)
    elif S1[i] not in nums and S2[i] in nums:
        checked.add(ord(S1[i]) - base)

    if S1[i] not in nums:
        alfs.add(ord(S1[i]) - base)
    if S2[i] not in nums:
        alfs.add(ord(S2[i]) - base)

black_list = set()
ans = 1
for c in checked:
    black_list.add(ufpc.find(c))
for alf in alfs:
    if ufpc.find(alf) not in black_list:
        f = chr(alf + base)
        if f in [S1[0], S2[0]]:
            ans *= 9
        else:
            ans *= 10
        black_list.add(ufpc.find(alf))
print(ans)
