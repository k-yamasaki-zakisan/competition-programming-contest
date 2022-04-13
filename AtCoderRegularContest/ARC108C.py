# https://atcoder.jp/contests/arc108/tasks/arc108_c

from collections import deque

N, M = map(int, input().split())
UVC = [list(map(int, input().split())) for _ in range(M)]
root = [[] for _ in range(N)]
for u, v, c in UVC:
    u, v = u - 1, v - 1
    root[u].append((v, c))
    root[v].append((u, c))
dp = [-1] * N
dp[0] = 1
stack = deque([0])
while len(stack):
    now = stack.popleft()
    for next, c in root[now]:
        if dp[next] != -1:
            continue
        if dp[now] == c:
            dp[next] = 1 if c != 1 else 2
        else:
            dp[next] = c
        stack.append(next)
for d in dp:
    print(d)
