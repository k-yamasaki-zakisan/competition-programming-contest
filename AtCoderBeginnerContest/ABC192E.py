# https://atcoder.jp/contests/abc192/tasks/abc192_e

from collections import defaultdict  # 辞書の初期値
from collections import Counter
import re
import copy
import itertools
from sys import stdin
from collections import deque
from copy import copy
from itertools import combinations
import heapq
import sys
input = sys.stdin.readline
# memo = defaultdict(int)

INF = float('inf')
N, M, X, Y = map(int, input().split())
X -= 1
Y -= 1
root = [[] for _ in range(N)]
for _ in range(M):
    a, b, t, k = map(int, input().split())
    a -= 1
    b -= 1
    root[b].append([a, t, k])
    root[a].append([b, t, k])

stack = deque([X])
time = [INF]*N
time[X] = 0
while 0 < len(stack):
    v = stack.popleft()
    for i, t, k in root[v]:
        if time[v] % k == 0:
            next_time = time[v]+t
        else:
            next_time = (1+time[v]//k)*k+t
        if next_time < time[i]:
            time[i] = next_time
            stack.append(i)

if time[Y] == INF:
    print(-1)
else:
    print(time[Y])
