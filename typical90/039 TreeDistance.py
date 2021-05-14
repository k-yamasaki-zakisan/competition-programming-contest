# https://atcoder.jp/contests/typical90/tasks/typical90_am

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]


def dps(pos: int, pre: int) -> None:
    dp[pos] = 1
    for i in root[pos]:
        if i == pre:
            continue
        dps(i, pos)
        dp[pos] += dp[i]


root = [[] for _ in range(N)]
dp = [0]*N
for a, b in AB:
    a, b = a-1, b-1
    root[a].append(b)
    root[b].append(a)

dps(0, -1)
ans = 0
for a, b in AB:
    a, b = a-1, b-1
    r = min(dp[a], dp[b])
    ans += r*(N-r)

print(ans)
