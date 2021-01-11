# https://atcoder.jp/contests/abc188/tasks/abc188_e

from collections import deque
INF = float('inf')
N, M = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]
graph = [[]*N for _ in range(N)]
for x, y in XY:
    x, y = x-1, y-1
    graph[x].append(y)
dp = [INF]*N
ans = -INF
for j in range(N):
    if dp[j] != INF:
        continue
    stack = deque([j])
    dp[j] = A[j]
    while len(stack):
        p = stack.popleft()
        for i in graph[p]:
            if min(dp[p], A[p]) < dp[i]:
                dp[i] = min(dp[p], A[p])
                stack.append(i)
ans = -INF
for i in range(N):
    if A[i] == dp[i]:
        continue
    ans = max(ans, A[i]-dp[i])
print(ans)
