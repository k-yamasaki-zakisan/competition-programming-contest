# https://atcoder.jp/contests/arc060/tasks/arc060_a

import sys

sys.stdin.readline
sys.setrecursionlimit(10**7)
MOD = 10**9 + 7
INF = float("inf")

N, A = map(int, input().split())
X = list(map(int, input().split()))
dp = [[0] * (50 * N + 1) for _ in range(N + 1)]
dp[0][0] = 1
for x in X:
    for i in range(N + 1, 0, -1):
        for j in range(50 * N + 1):
            if 0 <= j - x and dp[i - 1][j - x] != 0:
                dp[i][j] += dp[i - 1][j - x]
ans = 0
for i in range(1, N + 1):
    ans += dp[i][i * A]
print(ans)
