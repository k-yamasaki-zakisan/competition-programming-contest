# https://atcoder.jp/contests/abc220/tasks/abc220_f
# 再帰関数はpypyよりpythonの方が速い可能性がある

from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]


def dps(pos: int, pre: int) -> None:
    dp[pos] = 1
    for i in root[pos]:
        if dp[i] != -1:
            continue
        dist[i] = dist[pos]+1
        dps(i, pos)
        dp[pos] += dp[i]


root = [[] for _ in range(N)]
dp = [-1]*N
dp[0] = 0
dist = [-1]*N
dist[0] = 0
for a, b in AB:
    a, b = a-1, b-1
    root[a].append(b)
    root[b].append(a)

dps(0, -1)

ans = [-1]*N
ans[0] = sum(dist)
stack = deque([0])
while len(stack):
    now = stack.popleft()
    for v in root[now]:
        if ans[v] == -1:
            ans[v] = ans[now]+N-2*dp[v]
            stack.append(v)

for a in ans:
    print(a)
