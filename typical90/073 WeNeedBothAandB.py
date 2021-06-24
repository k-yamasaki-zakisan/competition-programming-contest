# https://atcoder.jp/contests/typical90/tasks/typical90_bu

import sys
sys.setrecursionlimit(10 ** 7)

MOD = 1000000007


def dps(pos: int, pre: int):
    val1, val2 = 1, 1
    for i in ROOT[pos]:
        if i == pre:
            continue
        dps(i, pos)
        if C[pos] == 'a':
            val1 *= dp[i][0] + dp[i][2]
            val2 *= (dp[i][0] + dp[i][1] + 2 * dp[i][2])

        if C[pos] == 'b':
            val1 *= dp[i][1] + dp[i][2]
            val2 *= (dp[i][0] + dp[i][1] + 2 * dp[i][2])

        val1 %= MOD
        val2 %= MOD

    if C[pos] == 'a':
        dp[pos][0] = val1
        dp[pos][2] = (val2-val1+MOD) % MOD
    if C[pos] == 'b':
        dp[pos][1] = val1
        dp[pos][2] = (val2-val1+MOD) % MOD


N = int(input())
C = list(map(str, input().split()))
AB = [list(map(int, input().split())) for _ in range(N-1)]
dp = [[0]*3 for _ in range(N)]
ROOT = [[] for _ in range(N)]
for a, b in AB:
    a, b = a-1, b-1
    ROOT[a].append(b)
    ROOT[b].append(a)

dps(0, -1)
print(dp[0][2])
