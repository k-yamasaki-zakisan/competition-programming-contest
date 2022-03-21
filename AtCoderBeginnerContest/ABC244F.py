# https://atcoder.jp/contests/abc244/tasks/abc244_f

from collections import deque
import sys

sys.stdin.readline
sys.setrecursionlimit(10**7)


INF = float("inf")
MOD1 = 10**9 + 7
MOD2 = 998244353

N, M = map(int, input().split())
E = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    E[u].append(v)
    E[v].append(u)
for i in range(N):
    E[N].append(i)

stack = deque([(0, N)])
dp = [[10**10] * (N + 1) for i in range(2**N)]
dp[0][N] = 0

V = [[-1] * (N + 1) for i in range(2**N)]
while stack:
    bit, now = stack.popleft()
    for nex in E[now]:
        bbit = bit ^ (1 << nex)
        if V[bbit][nex] == -1:
            V[bbit][nex] = 1
            dp[bbit][nex] = dp[bit][now] + 1
            stack.append((bbit, nex))
ans = 0
for i in range(2**N):
    ans += min(dp[i])
print(ans)
