# https://atcoder.jp/contests/typical90/tasks/typical90_ap

MOD = 10**9+7
N = int(input())
if N % 9:
    print(0)
    exit()

dp = [0]*(N+1)
dp[0] = 1
for i in range(1, N+1):
    B = min(i, 9)
    for j in range(1, B+1):
        dp[i] += dp[i-j]
    dp[i] %= MOD
print(dp[N] % MOD)
