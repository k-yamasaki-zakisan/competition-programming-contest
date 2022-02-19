# https://atcoder.jp/contests/abc239/tasks/abc239_e

import sys
from collections import deque

sys.stdin.readline
sys.setrecursionlimit(10**7)
INF = float("inf")


N, Q = map(int, input().split())
X = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N - 1)]
VK = [list(map(int, input().split())) for _ in range(Q)]
root = [[] for _ in range(N)]
for a, b in AB:
    a, b = a - 1, b - 1
    root[a].append(b)
    root[b].append(a)
dist = [-1] * N
dist[0] = 0
stack = deque([0])
while len(stack):
    now = stack.popleft()
    for next in root[now]:
        if dist[next] == -1:
            dist[next] = dist[now] + 1
            stack.append(next)
priority = [(d, i) for i, d in enumerate(dist)]
priority = sorted(priority, key=lambda x: -x[0])
num_memo = [[] for _ in range(N)]
for p_d, now in priority:
    num_memo[now].append(X[now])
    for r in root[now]:
        if dist[r] - 1 == p_d:
            num_memo[now] += num_memo[r]
    num_memo[now].sort(reverse=True)
    num_memo[now] = num_memo[now][:20]

for v, k in VK:
    print(num_memo[v - 1][k - 1])
