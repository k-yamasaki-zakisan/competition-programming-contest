# https://atcoder.jp/contests/abc244/tasks/abc244_e

import sys

sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float("inf")
MOD1 = 10**9 + 7
MOD2 = 998244353

N, M, K, S, T, X = map(int, input().split())
S -= 1
T -= 1
X -= 1
UV = [list(map(int, input().split())) for _ in range(M)]
root = [[] for _ in range(N)]
for u, v in UV:
    u, v = u - 1, v - 1
    root[u].append(v)
    root[v].append(u)
dp = [[[0, 0] for _ in range(N)] for _ in range(K + 1)]
dp[0][S][0] = 1
for i in range(K):
    for now in range(N):
        for next in root[now]:
            for j in range(2):
                if next == X:
                    dp[i + 1][next][(j + 1) % 2] += dp[i][now][j]
                    dp[i + 1][next][(j + 1) % 2] %= MOD2
                else:
                    dp[i + 1][next][j] += dp[i][now][j]
                    dp[i + 1][next][j] %= MOD2
print(dp[-1][T][0] % MOD2)
