# https://atcoder.jp/contests/typical90/tasks/typical90_h

MOD = 10**9+7

N = int(input())
S = input()
dp = [[0]*(8) for _ in range(N+1)]
dp[0][0] = 1

for h in range(N):
    for w in range(8):
        dp[h+1][w] += dp[h][w]
        if (
            (S[h] == 'a' and w == 0) or
            (S[h] == 't' and w == 1) or
            (S[h] == 'c' and w == 2) or
            (S[h] == 'o' and w == 3) or
            (S[h] == 'd' and w == 4) or
            (S[h] == 'e' and w == 5) or
            (S[h] == 'r' and w == 6)
        ):
            dp[h+1][w+1] += dp[h][w]
    for w in range(8):
        dp[h+1][w] %= MOD

print(dp[-1][-1])
