# https://atcoder.jp/contests/typical90/tasks/typical90_bq

MOD = 10**9+7

N, K = map(int, input().split())
ans = K % MOD
if 0 < N-1:
    ans *= (K-1)
    ans %= MOD
if 0 < N-2:
    ans *= pow(K-2, N-2, MOD)
print(ans % MOD)
